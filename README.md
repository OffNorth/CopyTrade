# 🤖 CopyTrade

**CopyTrade** est un bot Telegram permettant d'automatiser des swaps sur **Solana** via **Jupiter**.

Le bot peut être installé et exécuté sur :

* 🪟 Windows
* 🐧 Linux
* 📱 Termux / Android

> ⚠️ **Attention :** le bot peut effectuer de vraies transactions sur le réseau Solana. Utilisez uniquement un wallet dédié et ne stockez jamais votre clé privée directement dans le code.

---

## ✨ Fonctionnalités

* 🔄 Achat puis vente automatique d'un token
* 🤖 Contrôle via Telegram
* 🪙 Choix du token à utiliser
* ⚡ Swaps via Jupiter
* 🌐 Compatible Solana Mainnet
* 🔐 Configuration avec `.env`
* 🪟 Windows
* 🐧 Linux
* 📱 Termux

---

# 📁 Structure du projet

```text
CopyTrade/
├── bot.py
├── requirements.txt
└── README.md
```

---

# 🔧 Prérequis

Avant de commencer, vous devez avoir :

* Python **3.10 ou supérieur**
* Un bot Telegram
* Un wallet Solana
* Une clé privée Solana au format Base58
* Une adresse RPC Solana
* Des SOL pour payer les frais de transaction

---

# 🔐 Configuration `.env`

Les informations sensibles doivent être placées dans un fichier `.env`.

Créez :

```text
.env
```

Puis ajoutez :

```env
TELEGRAM_TOKEN=TON_TOKEN_TELEGRAM
RPC_URL=https://api.mainnet-beta.solana.com
PRIVATE_KEY=TA_CLE_PRIVEE_BASE58
TOKEN_ADDRESS=ADRESSE_DU_TOKEN

AMOUNT_PER_SWAP=0.005
SLIPPAGE_BPS=100
DELAY_BETWEEN_CYCLES=15
```

### Description

| Variable               | Description                     |
| ---------------------- | ------------------------------- |
| `TELEGRAM_TOKEN`       | Token fourni par @BotFather     |
| `RPC_URL`              | RPC utilisé pour Solana         |
| `PRIVATE_KEY`          | Clé privée du wallet en Base58  |
| `TOKEN_ADDRESS`        | Mint address du token           |
| `AMOUNT_PER_SWAP`      | Montant de SOL utilisé par swap |
| `SLIPPAGE_BPS`         | Slippage en basis points        |
| `DELAY_BETWEEN_CYCLES` | Délai entre les opérations      |

### Exemple

```env
AMOUNT_PER_SWAP=0.005
SLIPPAGE_BPS=100
DELAY_BETWEEN_CYCLES=15
```

Ici :

* `0.005` = 0.005 SOL par swap
* `100` = 1 % de slippage
* `15` = 15 secondes

---

# 🛡️ Sécurité

**Ne partagez jamais votre clé privée.**

Ne mettez jamais votre `.env` sur GitHub.

Ajoutez un fichier :

```text
.gitignore
```

avec :

```gitignore
.env
venv/
.venv/
__pycache__/
*.pyc
```

Vous pouvez publier :

```text
.env.example
```

avec uniquement des valeurs fictives :

```env
TELEGRAM_TOKEN=YOUR_TELEGRAM_TOKEN
RPC_URL=https://api.mainnet-beta.solana.com
PRIVATE_KEY=YOUR_PRIVATE_KEY
TOKEN_ADDRESS=YOUR_TOKEN_ADDRESS

AMOUNT_PER_SWAP=0.005
SLIPPAGE_BPS=100
DELAY_BETWEEN_CYCLES=15
```

---

# 📦 Installation

## 🪟 Windows

### 1. Installer Python

Téléchargez Python depuis :

https://www.python.org/downloads/

Pendant l'installation, cochez :

```text
Add Python to PATH
```

Vérifiez ensuite :

```powershell
python --version
```

---

### 2. Télécharger le projet

Avec Git :

```powershell
git clone https://github.com/OffNorth/CopyTrade.git
cd CopyTrade
```

Ou téléchargez le projet en ZIP depuis GitHub puis décompressez-le.

---

### 3. Créer l'environnement virtuel

```powershell
python -m venv venv
```

Activez-le :

```powershell
venv\Scripts\activate
```

---

### 4. Installer les dépendances

```powershell
pip install -r requirements.txt
```

---

### 5. Créer `.env`

```powershell
copy .env.example .env
```

Puis ouvrez `.env` et remplissez vos informations.

---

### 6. Lancer CopyTrade

```powershell
python bot.py
```

Le terminal doit afficher que le bot est démarré.

---

# 🐧 Installation Linux

## 1. Installer Python et Git

Sur Ubuntu / Debian :

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git -y
```

Vérifiez :

```bash
python3 --version
```

---

## 2. Télécharger le projet

```bash
git clone https://github.com/OffNorth/CopyTrade.git
cd CopyTrade
```

---

## 3. Créer l'environnement virtuel

```bash
python3 -m venv venv
```

Activez-le :

```bash
source venv/bin/activate
```

---

## 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 5. Configurer `.env`

```bash
cp .env.example .env
```

Éditez le fichier :

```bash
nano .env
```

Ajoutez vos informations :

```env
TELEGRAM_TOKEN=TON_TOKEN
RPC_URL=https://api.mainnet-beta.solana.com
PRIVATE_KEY=TA_CLE_PRIVEE
TOKEN_ADDRESS=TON_TOKEN_ADDRESS

AMOUNT_PER_SWAP=0.005
SLIPPAGE_BPS=100
DELAY_BETWEEN_CYCLES=15
```

Enregistrez avec :

```text
CTRL + O
ENTER
CTRL + X
```

---

## 6. Lancer le bot

```bash
python3 bot.py
```

---

# 📱 Installation Termux

CopyTrade peut être exécuté directement depuis Android avec **Termux**.

### 1. Installer Termux

Installez une version récente de Termux.

---

### 2. Mettre à jour Termux

```bash
pkg update
pkg upgrade
```

---

### 3. Installer Python et Git

```bash
pkg install python git -y
```

Vérifiez Python :

```bash
python --version
```

---

### 4. Télécharger CopyTrade

```bash
git clone https://github.com/OffNorth/CopyTrade.git
cd CopyTrade
```

---

### 5. Créer l'environnement virtuel

```bash
python -m venv venv
```

Activez-le :

```bash
source venv/bin/activate
```

---

### 6. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

### 7. Configurer `.env`

```bash
cp .env.example .env
```

Puis :

```bash
nano .env
```

Remplissez :

```env
TELEGRAM_TOKEN=TON_TOKEN
RPC_URL=https://api.mainnet-beta.solana.com
PRIVATE_KEY=TA_CLE_PRIVEE
TOKEN_ADDRESS=TON_TOKEN_ADDRESS

AMOUNT_PER_SWAP=0.005
SLIPPAGE_BPS=100
DELAY_BETWEEN_CYCLES=15
```

---

### 8. Lancer CopyTrade

```bash
python bot.py
```

Tant que Termux reste actif, le bot peut continuer à fonctionner.

---

# 📦 requirements.txt

Le fichier `requirements.txt` doit contenir les dépendances nécessaires :

```txt
python-telegram-bot
httpx
solana
solders
base58
```

Installation manuelle possible avec :

```bash
pip install python-telegram-bot httpx solana solders base58
```

---

# 🤖 Configuration Telegram

1. Ouvrez Telegram.
2. Cherchez **@BotFather**.
3. Utilisez :

```text
/newbot
```

4. Choisissez un nom pour votre bot.
5. Choisissez son username.
6. BotFather vous donnera un token.

Exemple :

```text
123456789:AAxxxxxxxxxxxxxxxxxxxxxxxx
```

Placez-le dans :

```env
TELEGRAM_TOKEN=123456789:AAxxxxxxxxxxxxxxxxxxxxxxxx
```

---

# 🎮 Commandes Telegram

Une fois le bot lancé :

### `/start`

Affiche les commandes disponibles.

```text
/start
```

### `/set_token`

Définit le token à utiliser.

```text
/set_token ADRESSE_DU_TOKEN
```

### `/start_volume`

Lance les cycles automatiques.

```text
/start_volume
```

### `/stop_volume`

Arrête les cycles.

```text
/stop_volume
```

### `/status`

Affiche l'état actuel du bot.

```text
/status
```

---

# 🔄 Fonctionnement

Le fonctionnement général est :

```text
        Telegram
            │
            ▼
      ┌─────────────┐
      │  CopyTrade  │
      └──────┬──────┘
             │
             ▼
         Jupiter API
             │
       ┌─────┴─────┐
       ▼           ▼
      SOL        TOKEN
       │           │
       └─────┬─────┘
             │
             ▼
       Solana Mainnet
```

Lorsqu'un cycle est lancé :

```text
SOL
 │
 ▼
ACHAT TOKEN
 │
 │ attente
 ▼
VENTE TOKEN
 │
 ▼
SOL
 │
 ▼
Nouveau cycle
```

---

# ⚠️ Risques

Ce bot effectue des transactions réelles lorsqu'il est configuré avec un wallet Mainnet.

Les pertes peuvent notamment provenir de :

* Slippage
* Frais réseau
* Frais de swap
* Faible liquidité
* Variation du prix
* Échec d'une transaction
* Mauvaise adresse de token
* Problème RPC
* Bug logiciel

**Utilisez un wallet dédié avec uniquement les fonds nécessaires.**

---

# 🧪 Recommandation avant utilisation

Avant d'utiliser CopyTrade avec des fonds importants :

1. Utilisez un wallet dédié.
2. Vérifiez l'adresse du token.
3. Vérifiez le montant du swap.
4. Vérifiez le slippage.
5. Testez avec une très petite quantité.
6. Vérifiez les transactions sur Solana Explorer.
7. Vérifiez les logs du bot.

---

# 🛠️ Dépannage

### `ModuleNotFoundError`

Réinstallez les dépendances :

```bash
pip install -r requirements.txt
```

---

### Python introuvable

Windows :

```powershell
python --version
```

Linux / Termux :

```bash
python3 --version
```

Si Python n'est pas installé, installez-le avec le gestionnaire de paquets correspondant.

---

### Erreur Telegram

Vérifiez :

```env
TELEGRAM_TOKEN=...
```

Le token doit être celui fourni par `@BotFather`.

---

### Erreur RPC

Vérifiez :

```env
RPC_URL=https://api.mainnet-beta.solana.com
```

Vous pouvez également utiliser un RPC dédié comme Helius ou QuickNode.

---

### Erreur de transaction

Vérifiez :

* Votre solde SOL
* L'adresse du token
* Le slippage
* La liquidité du token
* Le RPC
* Les logs du bot

---

# 📄 Licence

Ce projet est fourni à des fins éducatives et expérimentales.

L'utilisation du logiciel et des transactions effectuées avec celui-ci relève de la responsabilité de l'utilisateur.

---

# 👤 Auteur

**ZigXBT**

GitHub : [@OffNorth](https://github.com/OffNorth)

X / Twitter : [@zigxbt](https://x.com/zigxbt)

Instagram : [@zigxbt](https://instagram.com/zigxbt)

TikTok : [@zigxbt](https://tiktok.com/@zigxbt)

---

# ⭐ Support

Si le projet vous est utile, vous pouvez laisser une ⭐ au repository GitHub.

**CopyTrade — Solana Telegram Bot**
