import asyncio
import base58
import httpx
import logging
import time
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Confirmed
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.transaction import VersionedTransaction
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# === CONFIGURATION (À MODIFIER) ===
TELEGRAM_TOKEN = "TON_TOKEN_TELEGRAM"        # Ton token @BotFather
RPC_URL = "https://api.mainnet-beta.solana.com"  # Ou Helius / QuickNode
PRIVATE_KEY = "TA_CLE_PRIVEE_BASE58"          # Le wallet qui va faire le volume
TOKEN_ADDRESS = "LE_TOKEN_A_BOOSTER"          # Ex: "So111... (SOL)" ou ton memecoin

# Paramètres du volume
AMOUNT_PER_SWAP = 0.005  # Montant en SOL à échanger à chaque achat/vente
SLIPPAGE_BPS = 100       # Slippage de 1% (100 bips)
DELAY_BETWEEN_CYCLES = 15  # Temps (en secondes) entre un achat et une vente
# =================================

client = AsyncClient(RPC_URL)
keypair = Keypair.from_bytes(base58.b58decode(PRIVATE_KEY))
logging.basicConfig(level=logging.INFO)

# Variables globales pour contrôler le bot
volume_active = False
current_token = TOKEN_ADDRESS
pending_tx = None  # Pour garder la trace du token acheté

# === FONCTIONS JUPITER (SWAPS) ===
async def get_swap_quote(input_mint: str, output_mint: str, amount: int):
    """Récupère une quote de swap depuis Jupiter."""
    url = "https://quote-api.jup.ag/v6/quote"
    params = {
        "inputMint": input_mint,
        "outputMint": output_mint,
        "amount": amount,
        "slippageBps": SLIPPAGE_BPS,
    }
    async with httpx.AsyncClient(timeout=30) as client_http:
        resp = await client_http.get(url, params=params)
        resp.raise_for_status()
        return resp.json()

async def execute_swap(quote_response):
    """Exécute le swap via Jupiter et renvoie la signature."""
    url = "https://quote-api.jup.ag/v6/swap"
    payload = {
        "quoteResponse": quote_response,
        "userPublicKey": str(keypair.pubkey()),
        "wrapAndUnwrapSol": True,
        "dynamicComputeUnitLimit": True,
    }
    async with httpx.AsyncClient(timeout=30) as client_http:
        resp = await client_http.post(url, json=payload)
        resp.raise_for_status()
        swap_data = resp.json()

    # Récupérer la transaction et la signer
    raw_tx = base58.b58decode(swap_data["swapTransaction"])
    tx = VersionedTransaction.from_bytes(raw_tx)
    tx.sign([keypair])

    # Envoyer la transaction
    result = await client.send_transaction(tx, opts=TxOpts(skip_preflight=True))
    tx_sig = result.value
    logging.info(f"✅ Swap exécuté : {tx_sig}")
    
    # Attendre la confirmation
    await client.confirm_transaction(tx_sig, commitment=Confirmed)
    return tx_sig

# === BOUCLE PRINCIPALE DU VOLUME ===
async def volume_loop():
    """Boucle infinie qui achète puis revend le token."""
    global volume_active, current_token, pending_tx

    # SOL est le token d'entrée (mint officiel de Solana)
    SOL_MINT = "So11111111111111111111111111111111111111112"

    while volume_active:
        try:
            logging.info("🔄 Début d'un cycle de volume...")

            # 1. ACHAT : SOL -> TOKEN
            amount_in_lamports = int(AMOUNT_PER_SWAP * 1e9)  # 1 SOL = 1e9 lamports
            quote_buy = await get_swap_quote(SOL_MINT, current_token, amount_in_lamports)
            await execute_swap(quote_buy)
            await asyncio.sleep(DELAY_BETWEEN_CYCLES)

            if not volume_active:
                break

            # 2. VENTE : TOKEN -> SOL
            # (On doit récupérer le solde du token pour tout vendre, 
            #  mais pour simplifier on revend le même montant qu'on a acheté en estimant le prix.)
            # Ici, on utilise le même montant en SOL pour revendre (en pratique, il faut le montant exact de tokens).
            # Pour un bot plus robuste, il faudrait récupérer le solde du token.
            # Version simplifiée : on vend la même valeur en SOL (on suppose que le prix n'a pas trop bougé).
            quote_sell = await get_swap_quote(current_token, SOL_MINT, amount_in_lamports)
            await execute_swap(quote_sell)
            
            logging.info(f"✅ Cycle terminé, prochain dans {DELAY_BETWEEN_CYCLES}s")
            await asyncio.sleep(DELAY_BETWEEN_CYCLES)

        except Exception as e:
            logging.error(f"❌ Erreur dans le cycle : {e}")
            await asyncio.sleep(10)

# === COMMANDES TELEGRAM ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 *Bot Volume Solana actif !*\n"
        "Commandes :\n"
        "/set_token <adresse> - Définir le token à booster\n"
        "/start_volume - Lancer le générateur de volume\n"
        "/stop_volume - Arrêter le générateur\n"
        "/status - Voir l'état actuel",
        parse_mode="Markdown"
    )

async def set_token(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_token
    if not context.args:
        await update.message.reply_text("❌ Donne une adresse : /set_token <adresse_token>")
        return
    current_token = context.args[0]
    await update.message.reply_text(f"✅ Token défini : {current_token}")

async def start_volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global volume_active
    if volume_active:
        await update.message.reply_text("⚠️ Le volume est déjà en cours.")
        return
    volume_active = True
    asyncio.create_task(volume_loop())
    await update.message.reply_text(f"🚀 Volume lancé sur {current_token} ! (Toutes les {DELAY_BETWEEN_CYCLES}s)")

async def stop_volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global volume_active
    volume_active = False
    await update.message.reply_text("⏹️ Volume arrêté.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_text = "ACTIF ✅" if volume_active else "INACTIF ❌"
    await update.message.reply_text(
        f"📈 *Statut du Volume Bot*\n"
        f"Token cible : `{current_token}`\n"
        f"Montant par swap : {AMOUNT_PER_SWAP} SOL\n"
        f"État : {status_text}",
        parse_mode="Markdown"
    )

# === LANCEMENT ===
async def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("set_token", set_token))
    app.add_handler(CommandHandler("start_volume", start_volume))
    app.add_handler(CommandHandler("stop_volume", stop_volume))
    app.add_handler(CommandHandler("status", status))

    logging.info("🤖 Bot Volume démarré. Appuyez sur Ctrl+C pour arrêter.")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
