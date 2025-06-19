# parser.py

import asyncio
from playwright.async_api import async_playwright

async def check_slots():
    url = "https://visa.vfsglobal.com/rus/en/fra/application-detail"

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url, timeout=60000)
            await page.wait_for_timeout(5000)  # Подождать 5 секунд

            content = await page.content()

            if "No appointment slots" in content or "нет доступных слотов" in content.lower():
                return False, "Пока нет доступных слотов 😞"
            else:
                return True, "🎉 Есть доступные слоты на VFS! Проверь сайт!"

    except Exception as e:
        return False, f"Ошибка при проверке сайта: {e}"