from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "Agent Server is running"

@app.route("/agent-api", methods=["POST"])
def webhook():
    data = request.get_json()
    if not data or "message" not in data:
        return {"ok": True}
    
    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")
    
    if text == "/start":
        reply_text = "هلا فيك! البوت شغال 100% ✅"
    else:
        reply_text = f"وصلتني رسالتك: {text}"
    
    send_message(chat_id, reply_text)
    return {"ok": True}

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
