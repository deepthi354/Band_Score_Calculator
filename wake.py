from playwright.sync_api import sync_playwright
import time
import random
import os

SCREENSHOT_DIR = os.path.join(os.getcwd(), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

APPS = [
    ("https://ielts-band-calculator.streamlit.app/", "band_calc_app"),
]

LAUNCH_ARGS = [
    "--disable-blink-features=AutomationControlled",
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-infobars",
    "--window-size=1366,768",
    "--start-maximized",
]

def human_delay(min_ms=800, max_ms=2200):
    time.sleep(random.uniform(min_ms, max_ms) / 1000)

def wake_app(playwright, url, prefix):
    print(f"\n--- Waking: {url} ---")

    browser = playwright.chromium.launch(
        headless=True,
        args=LAUNCH_ARGS,
    )

    context = browser.new_context(
        viewport={"width": 1366, "height": 768},
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        locale="en-US",
        timezone_id="America/Toronto",
        extra_http_headers={
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        },
    )

    context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });
        Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
        window.chrome = { runtime: {} };
    """)

    page = context.new_page()

    try:
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        human_delay(2000, 4000)

        page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"{prefix}_1_after_load.png"), full_page=True)
        print(f"  Screenshot 1 saved (after initial load)")

        body_text = page.inner_text("body")
        print(f"  Page text preview: {body_text[:300]}")

        wake_button_selector = "button:has-text('Yes, get this app back up!')"
        try:
            page.wait_for_selector(wake_button_selector, timeout=12000)
            print("  Sleep screen detected — clicking wake button...")
            human_delay()
            page.click(wake_button_selector)
            print("  Wake button clicked.")
            human_delay(6000, 9000)

            page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"{prefix}_2_after_wake_click.png"), full_page=True)
            print(f"  Screenshot 2 saved (after wake button click)")

        except Exception:
            print("  No sleep screen / wake button found.")
            page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"{prefix}_2_no_wake_button.png"), full_page=True)
            print(f"  Screenshot 2b saved (no wake button state)")

        try:
            page.wait_for_selector(
                "[data-testid='stAppViewContainer']",
                timeout=60000
            )
            print("  App container loaded successfully.")

            page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"{prefix}_3_app_loaded.png"), full_page=True)
            print(f"  Screenshot 3 saved (app fully loaded)")

        except Exception:
            print("  WARNING: App container did not appear.")
            page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"{prefix}_3_load_failed.png"), full_page=True)
            print(f"  Screenshot 3 saved (load failed state)")

        human_delay(1000, 2000)
        page.mouse.move(random.randint(300, 800), random.randint(200, 500))
        human_delay(500, 1200)
        page.evaluate("window.scrollBy(0, 120)")
        human_delay(1000, 2000)

        print("  Done.")

    except Exception as e:
        print(f"  ERROR: {e}")
        try:
            page.screenshot(path=os.path.join(SCREENSHOT_DIR, f"{prefix}_error.png"), full_page=True)
            print(f"  Error screenshot saved")
        except:
            pass

    finally:
        context.close()
        browser.close()


with sync_playwright() as playwright:
    for app_url, prefix in APPS:
        wake_app(playwright, app_url, prefix)
        human_delay(4000, 8000)