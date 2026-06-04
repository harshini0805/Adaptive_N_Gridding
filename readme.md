# Adaptive N-Gridding for UI Legibility in VLMs

## Overview

Vision-Language Models lose fine UI details (small text, labels, tables) due to patch-level compression.  
This project improves UI understanding by splitting screenshots into adaptive regions before VLM/OCR processing.

Goal: maximize UI legibility under a fixed vision-token budget.

---

## Components

### Ingestion

Input is either a URL or a screenshot. URLs are captured using Playwright. The system extracts viewport width, viewport height, device context, and full-page screenshot metadata.

---

### Image Analysis

Image properties such as size, aspect ratio, scroll ratio, and long-page detection are computed.

---

### Density Estimation

Edge density is computed using OpenCV Canny filtering as a proxy for visual complexity.

---

### Adaptive Grid Planner

Grid strategy is selected based on layout signals.

Long-scroll pages are split vertically. Standard UIs use balanced grids. Dense interfaces use higher-resolution tiling.

Device type is derived from viewport metadata, not screenshot aspect ratio.

---

### Tile Generation

The image is cropped into regions. Each tile stores a bounding box, tile image path, and tile ID.

---

### Region Output

```json
{
  "region_id": 0,
  "region_type": "grid",
  "image_path": "tiles/tile_0.png",
  "bbox": {
    "x": 0,
    "y": 0,
    "w": 1440,
    "h": 1500
  }
}