import asyncio
from playwright.async_api import async_playwright
import pandas as pd

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.reviews.io/company-reviews/store/vodacom-co-za")

        reviews = []

        for page_num in range(20):  # Adjust number of pages as needed
            print(f"📄 Scraping page {page_num + 1}...")

            try:
                await page.wait_for_selector('#reviewsContainer', timeout=15000)
                await page.mouse.wheel(0, 5000)  # Scroll down
                await page.wait_for_timeout(3000)

                cards = await page.query_selector_all('[data-review-id]')
                print(f"🔍 Found {len(cards)} review blocks")

                for card in cards:
                    try:
                        # Grab all visible text from review block
                        raw_text = await card.inner_text()
                        rating_stars = await card.query_selector_all('[data-rating="true"] svg.filled')

                        if raw_text.strip():  # Skip empty blocks
                            reviews.append({
                                "raw_text": raw_text.strip(),
                                "rating": len(rating_stars)
                            })

                    except Exception as e:
                        print(f"⚠️ Skipped a review due to error: {e}")

                # Try to go to the next page
                next_btn = await page.query_selector('a[rel="next"]')
                if next_btn and await next_btn.is_enabled():
                    await next_btn.click()
                    await page.wait_for_timeout(3000)
                else:
                    print("✅ No more pages to click through.")
                    break

            except Exception as e:
                print(f"❌ Error on page {page_num + 1}: {e}")
                break

        await browser.close()

        # Save data
        df = pd.DataFrame(reviews)
        df.to_csv("reviewsio_playwright_raw.csv", index=False)
        print(f"\n✅ Done! Saved {len(df)} reviews to 'reviewsio_playwright_raw.csv'")

if __name__ == "__main__":
    asyncio.run(run())
