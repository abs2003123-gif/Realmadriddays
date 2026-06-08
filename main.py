from datetime import date
import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@realmadriddays"

START_DATE = date(2024, 6, 1)  # روز قهرمانی 15 رئال در UCL

today = date.today()
days = (today - START_DATE).days + 1

text = f"{days}امین روز داشتن ۱۵ قهرمانی لیگ قهرمانان"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={
        "chat_id": CHANNEL_ID,
        "text": text
    }
)
