# Photo Enhancer

A desktop batch enhancer for photos.

![Photo Enhancer cover](assets/readme-cover.svg)

## What it does

- loads a folder of JPG/JPEG/PNG images
- applies brightness, contrast, and saturation adjustments
- keeps the original files untouched
- writes enhanced copies with an `enhanced_` prefix

## Before / after

| Before | After |
| --- | --- |
| <img src="screenshots/Before.jpg" width="320" alt="Before enhancement"> | <img src="screenshots/After.jpg" width="320" alt="After enhancement"> |

<img src="screenshots/Interface.png" alt="Main application window" width="700">

## Run

```bash
git clone https://github.com/mertefekurt/PhotoEnchancer.git
cd PhotoEnchancer
python -m pip install -r requirements.txt
python src/image_processor_gui.py
```
