class RegionGenerator:

    def generate(self, tiles_metadata):

        regions = []

        for tile in tiles_metadata:

            regions.append(
                {
                    "region_id": tile["tile_id"],

                    "region_type": "grid",

                    "image_path": tile["tile_path"],

                    "bbox": {
                        "x": tile["x"],
                        "y": tile["y"],
                        "w": tile["width"],
                        "h": tile["height"]
                    }
                }
            )

        return regions