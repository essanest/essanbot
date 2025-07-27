from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze(input: TextInput):
    message = input.text.lower()

    if "بیدار" in message:
        return {"response": "حالت بیدار فعال شد. از این لحظه فقط با تأیید شما خرید/فروش انجام می‌شود ✅"}

    if "خواب" in message:
        return {"response": "حالت خواب فعال شد. بات مجاز است تا سقف ۳۰٪ سرمایه توکن مناسب بخرد 💤"}

    if "توکن مناسب" in message or "چی بخرم" in message:
        return {"response": "در حال بررسی بازار برای شکار توکن مناسب هستم... ⏳"}

    return {"response": "پیام دریافت شد. در حال پردازش... ✅"}
