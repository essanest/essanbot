import requests
from config import BOT_TOKEN, CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_telegram_message(text, reply_markup=None):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    if reply_markup:
        payload["reply_markup"] = reply_markup

    response = requests.post(url, json=payload)
    return response.json()


def get_updates():
    url = f"{BASE_URL}/getUpdates"
    response = requests.get(url)
    return response.json()


def parse_user_message(data):
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        return chat_id, text.strip()
    return None, None


def create_inline_keyboard(buttons):
    return {
        "inline_keyboard": [
            [{"text": b["text"], "callback_data": b["callback_data"]}] for b in buttons
        ]
    }
