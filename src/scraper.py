from playwright.sync_api import sync_playwright
import os

def fetch_chapter(url: str, out_dir: str = "output") -> str:
    os.makedirs(out_dir, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=os.path.join(out_dir, "chapter.png"))
        content = page.locator("#mw-content-text").inner_text()
        with open(os.path.join(out_dir, "chapter.txt"), "w", encoding="utf-8") as f:
            f.write(content)
        browser.close()
    return content
