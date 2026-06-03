from ingestion.url_capture import URLCapture

from preprocessing.image_analyzer import ImageAnalyzer
from preprocessing.density_analyzer import DensityAnalyzer


# -------------------------
# CONFIG
# -------------------------

INPUT_MODE = "url"     # "url" or "image"

IMAGE_PATH = "uploads/stripe_sample.png"

URL = "https://stripe.com"


# -------------------------
# MAIN
# -------------------------

def main():

    # -------------------------
    # Ingestion Layer
    # -------------------------

    if INPUT_MODE == "image":

        input_data = {
            "input_type": "image",
            "image_path": IMAGE_PATH
        }

    elif INPUT_MODE == "url":

        capture = URLCapture()

        input_data = capture.capture(
            url=URL,
            viewport_width=1440,
            viewport_height=900
        )

    else:
        raise ValueError("Invalid INPUT_MODE")

    image_path = input_data["image_path"]

    # -------------------------
    # Preprocessing
    # -------------------------

    image_analyzer = ImageAnalyzer()
    density_analyzer = DensityAnalyzer()

    image_metadata = image_analyzer.analyze(
        image_path
    )

    density_metadata = density_analyzer.analyze(
        image_path
    )

    # -------------------------
    # Merge Results
    # -------------------------

    analysis_report = {
        **input_data,
        **image_metadata,
        **density_metadata
    }

    # -------------------------
    # Output
    # -------------------------

    print("\n===== ANALYSIS REPORT =====\n")

    for key, value in analysis_report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()