import asyncio
from playwright.async_api import async_playwright

apps = [
    "https://visualx-lab-double-pendulum.streamlit.app",
    "https://visualx-lab-electronic-configuration.streamlit.app",
    "https://visualx-lab-lissajous.streamlit.app"
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for app in apps:
            try:
                print(f"Pinging {app}...")
                page = await browser.new_page()
                await page.goto(app, timeout=60000)
                await asyncio.sleep(5)  # Wait a bit to ensure the container wakes up
                await page.close()
                print(f"Successfully pinged {app}")
            except Exception as e:
                print(f"Failed to ping {app}: {e}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
