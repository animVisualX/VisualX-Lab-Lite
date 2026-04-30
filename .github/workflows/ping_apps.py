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

                # Wait for the app to either load normally or show the sleeping screen
                await asyncio.sleep(5)

                # Check for the wake up element using a more generic text selector
                button = page.locator("text=Yes, get this app back up!")
                if await button.count() > 0:
                    print(f"App {app} is sleeping. Clicking wake up button...")
                    # Click the first matching element
                    await button.first.click()
                    # Wait a bit for the app to start waking up
                    await asyncio.sleep(10)
                else:
                    print(f"App {app} is already awake or loading.")

                await page.close()
                print(f"Successfully processed {app}")
            except Exception as e:
                print(f"Failed to ping {app}: {e}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
