import requests
import time
import os

# Configurações via Variáveis de Ambiente (Segurança total)
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
LINK_AFILIADO = "https://www.binance.com/pt/referral/earn-together/refer2earn-usdc/claim?hl=pt&ref=GRO_28502_9GMCA&utm_source=default"

def enviar_telegram(msg):
    texto = f"🤖 **IA SINAL ATIVO**\n\n{msg}\n\n💰 **BINANCE:** {LINK_AFILIADO}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={texto}&parse_mode=Markdown"
    try:
        requests.get(url, timeout=10)
    except:
        pass

def obter_preco_binance(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        res = requests.get(url, timeout=10)
        return float(res.json()['price'])
    except:
        return None

if __name__ == "__main__":
    while True:
        preco = obter_preco_binance("BTCUSDT")
        if preco:
            enviar_telegram(f"⚡ IA MONITORIZANDO: BTC\nPreço Atual: ${preco:,.2f}")
        time.sleep(300) # Verifica a cada 5 minutos
