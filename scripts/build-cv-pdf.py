"""Regenerate assets/Tejas_Jammihal_CV.pdf from the /cv-print/ page.

Usage (from the repo root, after `bundle exec jekyll build`):
    pip install playwright && playwright install chromium
    python3 scripts/build-cv-pdf.py
"""
import asyncio
import pathlib

from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "_site" / "cv-print" / "index.html"
OUT = ROOT / "assets" / "Tejas_Jammihal_CV.pdf"


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(SRC.as_uri())
        await page.wait_for_timeout(300)
        await page.pdf(path=str(OUT), format="Letter", prefer_css_page_size=True, print_background=True)
        await browser.close()
    print(f"wrote {OUT}")


if __name__ == "__main__":
    asyncio.run(main())
