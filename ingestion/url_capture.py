from datetime import datetime
from playwright.sync_api import sync_playwright


class URLCapture:

    def classify_device(self, viewport_width):

        if viewport_width < 768:
            return "mobile"

        elif viewport_width < 1200:
            return "tablet"

        return "desktop"

    def capture(
        self,
        url,
        viewport_width=1440,
        viewport_height=900
    ):

        # Generate unique filename
        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        screenshot_path = (
            f"screenshots/capture_{timestamp}.png"
        )

        with sync_playwright() as p:

            browser = p.chromium.launch()

            page = browser.new_page(
                viewport={
                    "width": viewport_width,
                    "height": viewport_height
                }
            )

            page.goto(
                url,
                wait_until="networkidle"
            )

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

            "device_type": self.classify_device(
                viewport_width
            ),

            "capture_timestamp": datetime.now().isoformat(),

            "image_path": screenshot_path
        }