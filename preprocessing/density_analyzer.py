#To estimate visual density using edge density

#imports
import cv2
import numpy as np

class DensityAnalyzer:

    def edge_density(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError(
                f"Unable to load image: {image_path}"
            )

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        edges = cv2.Canny(
            gray,
            100,
            200
        )

        edge_pixels = np.count_nonzero(edges)

        density = edge_pixels / edges.size

        return round(float(density), 4)

    def analyze(self, image_path):

        return {
            "edge_density": self.edge_density(image_path)
        }