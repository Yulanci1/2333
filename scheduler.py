# scheduler.py

import asyncio
from parser import check_slots
from config import BOT_TOKEN, USER_CHAT_ID, CHECK_INTERVAL
from telegram import Bot

bot = Bot(token=BOT_TOKEN)

async def periodic_check():
    while True:
        available, message = await check_slots()
        if available:
            await bot.send_message(chat_id=USER_CHAT_ID, text=message)
        await asyncio.sleep(CHECK_INTERVAL)

def run_scheduler():
    asyncio.run(periodic_check())