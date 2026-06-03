from ingestion.url_capture import URLCapture

from preprocessing.image_analyzer import ImageAnalyzer
from preprocessing.density_analyzer import DensityAnalyzer

from planner.grid_planner import GridPlanner

from tiling.tile_generator import TileGenerator
from regions.region_generator import RegionGenerator


# -------------------------
# CONFIG
# -------------------------

INPUT_MODE = "url"      # "url" or "image"

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
    # Image Analysis
    # -------------------------

    image_analyzer = ImageAnalyzer()
    image_metadata = image_analyzer.analyze(
        image_path
    )

    # -------------------------
    # Density Analysis
    # -------------------------

    density_analyzer = DensityAnalyzer()

    density_metadata = density_analyzer.analyze(
        image_path
    )

    # -------------------------
    # Merge Analysis
    # -------------------------

    analysis_report = {
        **input_data,
        **image_metadata,
        **density_metadata
    }

    # -------------------------
    # Grid Planning
    # -------------------------

    planner = GridPlanner()

    grid_plan = planner.plan(
        analysis_report
    )

    analysis_report["grid_plan"] = grid_plan

    # -------------------------
    # Tile Generation
    # -------------------------

    tile_generator = TileGenerator()

    tiles_metadata = tile_generator.generate(
        image_path,
        grid_plan
    )

    analysis_report["num_tiles"] = len(
        tiles_metadata
    )

    analysis_report["tiles_metadata"] = (
        tiles_metadata
    )

    # -------------------------
    # Region Generation
    # -------------------------

    region_generator = RegionGenerator()

    regions = region_generator.generate(
        tiles_metadata
    )

    analysis_report["regions"] = regions

    # -------------------------
    # Output
    # -------------------------

    print("\n===== ANALYSIS REPORT =====\n")

    for key, value in analysis_report.items():

        if key not in [
            "tiles_metadata",
            "regions"
        ]:
            print(f"{key}: {value}")

    print("\n===== GENERATED TILES =====\n")

    for tile in tiles_metadata:
        print(tile)

    print("\n===== REGIONS =====\n")

    for region in regions:
        print(region)


if __name__ == "__main__":
    main()