# Photo Enhancer

![Photo Enhancer cover](assets/readme-cover.svg)

A desktop photo utility for batch enhancement. It keeps the workflow simple: choose an input folder, tune brightness/contrast/saturation, preview the direction, and write enhanced copies to an output folder.

## Screenshots

| Before | After |
| --- | --- |
| <img src="screenshots/Before.jpg" width="320" alt="Before enhancement"> | <img src="screenshots/After.jpg" width="320" alt="After enhancement"> |

<p align="center">
  <img src="screenshots/Interface.png" alt="Main application window" width="680" />
</p>

## Features

- Batch processing for JPG, JPEG, and PNG images
- Brightness, contrast, and saturation controls
- Saved preferences between sessions
- Progress tracking and cancel support
- Tkinter interface with Pillow/OpenCV processing

## Run locally

```bash
git clone https://github.com/mertefekurt/PhotoEnchancer.git
cd PhotoEnchancer
python -m pip install -r requirements.txt
python src/image_processor_gui.py
```

## Notes

Enhanced images are written with an `enhanced_` prefix, so the original files stay untouched.
