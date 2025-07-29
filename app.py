from flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    ticker = data.get("ticker")
    evento = data.get("evento")
    accion = data.get("accion")

    mensaje = f"📢 ALERTA: {ticker}\nEvento: {evento}\nAcción: {accion}"

    # Twilio credentials desde variables de entorno
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM")  # Ej: 'whatsapp:+14155238886'
    to_whatsapp = os.getenv("MY_WHATSAPP_TO")          # Ej: 'whatsapp:+54911XXXXXXXX'

    client.messages.create(
        body=mensaje,
        from_=from_whatsapp,
        to=to_whatsapp
    )

    return {"status": "Mensaje enviado"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
