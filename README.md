# Photo Enhancer

![Photo Enhancer cover](assets/readme-cover.svg)

A desktop batch enhancer for JPG, JPEG, and PNG files. It keeps originals untouched and writes processed copies with an `enhanced_` prefix.

## Processing path

![Processing diagram](assets/readme-diagram.svg)

| Before | After |
| --- | --- |
| <img src="screenshots/Before.jpg" width="320" alt="Before enhancement"> | <img src="screenshots/After.jpg" width="320" alt="After enhancement"> |

<img src="screenshots/Interface.png" alt="Main application window" width="700">

## Local run

```bash
git clone https://github.com/mertefekurt/PhotoEnchancer.git
cd PhotoEnchancer
python -m pip install -r requirements.txt
python src/image_processor_gui.py
```

## Notes

- Originals stay untouched.
- Processed files are written with a predictable prefix.
- The interface is intentionally small enough for quick batch work.
