from flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot activo"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", "Alerta desde TradingView")

    client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    client.messages.create(
        from_='whatsapp:+14155238886',
        to=os.environ['WHATSAPP_TO'],
        body=message
    )

    return 'Mensaje enviado por WhatsApp', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
