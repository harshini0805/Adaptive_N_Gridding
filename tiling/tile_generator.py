from pathlib import Path
from PIL import Image


class TileGenerator:

    def generate(self, image_path, grid_plan):

        strategy = grid_plan["strategy"]

        Path("tiles").mkdir(exist_ok=True)

        if strategy == "long_scroll":
            return self._long_scroll(
                image_path,
                grid_plan
            )

        elif strategy == "standard_grid":
            return self._grid(
                image_path,
                rows=2,
                cols=2,
                strategy=strategy
            )

        elif strategy == "dense_grid":
            return self._grid(
                image_path,
                rows=3,
                cols=3,
                strategy=strategy
            )

        raise ValueError(
            f"Unknown strategy: {strategy}"
        )

    def _long_scroll(
        self,
        image_path,
        grid_plan
    ):

        image = Image.open(image_path)

        width, height = image.size

        segment_height = grid_plan["segment_height"]
        overlap = grid_plan["overlap"]

        metadata = []

        start_y = 0
        tile_id = 0

        while start_y < height:

            end_y = min(
                start_y + segment_height,
                height
            )

            tile = image.crop(
                (
                    0,
                    start_y,
                    width,
                    end_y
                )
            )

            tile_path = (
                f"tiles/tile_{tile_id}.png"
            )

            tile.save(tile_path)

            metadata.append(
                {
                    "tile_id": tile_id,
                    "tile_path": tile_path,

                    "x": 0,
                    "y": start_y,

                    "width": width,
                    "height": end_y - start_y,

                    "strategy": "long_scroll"
                }
            )

            start_y += (
                segment_height - overlap
            )

            tile_id += 1

        return metadata

    def _grid(
        self,
        image_path,
        rows,
        cols,
        strategy
    ):

        image = Image.open(image_path)

        width, height = image.size

        tile_width = width // cols
        tile_height = height // rows

        metadata = []

        tile_id = 0

        for r in range(rows):

            for c in range(cols):

                x1 = c * tile_width
                y1 = r * tile_height

                x2 = (
                    width
                    if c == cols - 1
                    else (c + 1) * tile_width
                )

                y2 = (
                    height
                    if r == rows - 1
                    else (r + 1) * tile_height
                )

                tile = image.crop(
                    (
                        x1,
                        y1,
                        x2,
                        y2
                    )
                )

                tile_path = (
                    f"tiles/tile_{tile_id}.png"
                )

                tile.save(tile_path)

                metadata.append(
                    {
                        "tile_id": tile_id,
                        "tile_path": tile_path,

                        "x": x1,
                        "y": y1,

                        "width": x2 - x1,
                        "height": y2 - y1,

                        "strategy": strategy
                    }
                )

                tile_id += 1

        return metadata