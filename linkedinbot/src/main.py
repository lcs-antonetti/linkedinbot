from playwright.sync_api import sync_playwright
import navigator as nv

def main ():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        nv.doorkicker(page)
        nv.jobfinder(page)

        browser.close()

if __name__ == "__main__":
    main()