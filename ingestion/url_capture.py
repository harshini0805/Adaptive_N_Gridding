from playwright.sync_api import sync_playwright

class URLCapture:

    def capture(
        self,
        url,
        viewport_width=1440,
        viewport_height=900,
        screenshot_path="screenshots/capture.png"
    ):

        with sync_playwright() as p:

            browser = p.chromium.launch()

            page = browser.new_page(
                viewport={
                    "width": viewport_width,
                    "height": viewport_height
                }
            )

            page.goto(url)

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            browser.close()

        return {
            "input_type": "url",
            "url": url,

            "viewport_width": viewport_width,
            "viewport_height": viewport_height,

            "image_path": screenshot_path
        }