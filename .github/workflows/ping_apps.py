import asyncio
from playwright.async_api import async_playwright

# List of apps to keep alive
APPS = [
    "https://visualx-lab-double-pendulum.streamlit.app",
    "https://visualx-lab-electronic-configuration.streamlit.app",
    "https://visualx-lab-lissajous.streamlit.app"
]

async def wake_up_app(app_url, browser):
    try:
        print(f"\n[{app_url}] Opening page...")
        # Create a new browser context for each app to avoid shared state/cache
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to the app, waiting until network is mostly idle
        await page.goto(app_url, wait_until="networkidle", timeout=60000)

        # Wait a few seconds to let any client-side redirects or Streamlit loading screens settle
        await asyncio.sleep(5)

        # Check if the "Yes, get this app back up!" button exists
        # We use a broad locator that looks for exact text on buttons or links
        wake_up_button = page.locator("text='Yes, get this app back up!'")

        if await wake_up_button.count() > 0:
            print(f"[{app_url}] App is sleeping! Clicking wake up button...")
            await wake_up_button.first.click()
            # Wait for a bit after clicking to ensure the request is sent
            await asyncio.sleep(15)
            print(f"[{app_url}] Wake up signal sent successfully.")
        else:
            print(f"[{app_url}] App seems to be awake already (no wake up button found).")

        await context.close()
    except Exception as e:
        print(f"[{app_url}] Failed to process app. Error: {e}")

async def main():
    print("Starting Keep-Alive Process with Playwright...")
    async with async_playwright() as p:
        # Launch Chromium headless
        browser = await p.chromium.launch(headless=True)

        # Process each app sequentially
        for app in APPS:
            await wake_up_app(app, browser)

        await browser.close()
    print("Keep-Alive Process completed.")

if __name__ == "__main__":
    asyncio.run(main())
