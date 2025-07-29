from flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)

TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP = "whatsapp:+14155238886"  # número sandbox
DESTINATARIO = os.environ.get("WHATSAPP_TO")

client = Client(TWILIO_SID, TWILIO_TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    mensaje = f"📊 Alerta de TradingView:\n{data}"
    client.messages.create(
        body=mensaje,
        from_=TWILIO_WHATSAPP,
        to=DESTINATARIO
    )
    return "OK", 200

@app.route('/')
def home():
    return "Bot activo", 200
