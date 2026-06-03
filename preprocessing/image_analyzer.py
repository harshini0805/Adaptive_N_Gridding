#To Input Screenshot, Extract Metadata, Return Analysis

#Imports
from PIL import Image

class ImageAnalyzer:

    #Analysis
    def analyze(self, image_path):

        #Checking if the image path exists or not
        try:
            image = Image.open(image_path)
        except Exception as e:
            raise ValueError(f"Invalid image file: {e}")

        width, height = image.size

        return {
            "width": width,
            "height": height,

            "aspect_ratio": round(width / height, 2),
            "scroll_ratio": round(height / width, 2),

            "total_pixels": width * height,

            "is_long_scroll": (height / width) > 3
        }
       
"""### Current Code Review (Phase 1.1)

#### Fix Now

* **Swap condition order**:

  ```python
  if (height/width) > 3:
      ...
  if aspect_ratio < 0.7:
      ...
  ```

  Otherwise very long mobile screenshots get classified as `mobile` instead of `long_scroll`.

#### Good As-Is

* Clean class structure (`ImageAnalyzer`).
* Metadata extraction is correct.
* Error handling for invalid images is present.
* Output schema is extensible (`density_score`, `grid_strategy` placeholders).
* Classification reason is useful for debugging and demos.

#### Add Soon (Next Iterations)

* `file_size_bytes`
* `image_mode` (RGB, RGBA, etc.)
* `megapixels`
* Density metrics:

  * edge density
  * text density
  * component density
  * whitespace ratio

#### Add Later

* Screen types:

  * dashboard
  * landing_page
  * form
  * ecommerce
  * settings_page
* Token-budget-aware grid planning.
* Layout-aware segmentation instead of uniform tiling.
* RegionFocus integration.

#### Overall

Current implementation is a solid **Phase 1.1 MVP foundation**. After fixing the long-scroll condition, move directly to the **Density Analyzer**, since that's the component that makes the grid truly adaptive rather than just aspect-ratio aware.
"""