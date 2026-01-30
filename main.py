import requests
import time
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# --- MINI-SITE PARA O RENDER ACEITAR O PLANO FREE ---
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>IA Trading Online</h1></body></html>", "utf-8"))

def run_server():
    server = HTTPServer(('0.0.0.0', 10000), MyServer)
    server.serve_forever()

# --- CONFIGURAÇÕES E ROBÔ ---
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
LINK = "https://www.binance.com/pt/referral/earn-together/refer2earn-usdc/claim?hl=pt&ref=GRO_28502_9GMCA&utm_source=default"

def enviar_telegram(msg):
    texto = f"🤖 **IA SINAL ATIVO**\n\n{msg}\n\n💰 **BINANCE:** {LINK}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={texto}&parse_mode=Markdown"
    try:
        requests.get(url, timeout=10)
    except:
        pass

if __name__ == "__main__":
    threading.Thread(target=run_server).start()
    while True:
        try:
            res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
            preco = float(res.json()['price'])
            enviar_telegram(f"⚡ MONITORIZANDO: BTC\nPreço Atual: ${preco:,.2f}")
        except:
            pass
        time.sleep(300)
