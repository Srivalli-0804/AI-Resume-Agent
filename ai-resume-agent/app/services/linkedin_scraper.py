from playwright.async_api import async_playwright


async def scrape_linkedin_job(job_url):

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True
        )

        page = await browser.new_page()

        await page.goto(
            job_url,
            timeout=60000
        )

        title = await page.title()

        await browser.close()

        return {
            "title": title,
            "description": "test"
        }