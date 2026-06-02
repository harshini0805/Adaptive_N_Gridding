from preprocessing.image_analyzer import ImageAnalyzer
from preprocessing.density_analyzer import DensityAnalyzer

IMAGE_PATH = "uploads/stripe_sample.png"

def main():

    # Initialize analyzers
    image_analyzer = ImageAnalyzer()
    density_analyzer = DensityAnalyzer()

    # Analyze image metadata
    image_metadata = image_analyzer.analyze(IMAGE_PATH)

    # Analyze density
    density_score = density_analyzer.density_score(IMAGE_PATH)

    # Merge results
    image_metadata["density_score"] = density_score

    print("\n===== ANALYSIS REPORT =====")

    for key, value in image_metadata.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
    