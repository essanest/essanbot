import os
import asyncio
from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx

app = FastAPI()

TELEGRAM_BOT_TOKEN = "7988601127:AAFXcCLC94rdXTMNQ_YudTL0VqPBjuhdQ1w"
TELEGRAM_CHAT_ID = "256764836"
ESSAN_API_URL = "http://localhost:8001/analyze"

class TelegramUpdate(BaseModel):
    message: dict

@app.get("/")
async def root():
    return {"message": "EssanBot backend running"}

@app.post("/")
async def telegram_webhook(update: TelegramUpdate):
    user_message = update.message.get("text", "").lower()

    if "سلام" in user_message or "start" in user_message:
        await send_message("درود! بات فعال است و آماده دریافت پیام‌هاست ✅")
        return {"ok": True}

    if "وضعیت" in user_message:
        await send_message("بات آنلاین است و به‌درستی کار می‌کند ✅")
        return {"ok": True}

    # ارسال پیام به ماژول تحلیلگر
    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(ESSAN_API_URL, json={"text": user_message})
            result = res.json()
            response = result.get("response", "پاسخی دریافت نشد ❌")
            await send_message(response)
    except Exception as e:
        await send_message(f"❌ خطا در ارتباط با ماژول تحلیلگر: {str(e)}")

    return {"ok": True}

async def send_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    async with httpx.AsyncClient() as client:
        await client.post(url, json=payload)
