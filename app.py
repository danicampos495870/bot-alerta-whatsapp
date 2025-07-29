from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Bot WhatsApp activo"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Datos recibidos:", data)
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run()


