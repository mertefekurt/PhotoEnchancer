from PIL import Image, ImageEnhance

DEFAULT_BRIGHTNESS = 1.27
DEFAULT_CONTRAST = 1.1
DEFAULT_SATURATION = 1.05


class ImageEnhancer:
    """Apply a consistent brightness, contrast, and saturation pass to images."""

    def __init__(self):
        """Initialize default enhancement factors used by the GUI."""
        self.brightness_factor = DEFAULT_BRIGHTNESS
        self.contrast_factor = DEFAULT_CONTRAST
        self.saturation_factor = DEFAULT_SATURATION

    def process_image(self, input_path, output_path):
        """Enhance a single image and save it to the requested output path.

        Returns:
            bool: True when the image is saved successfully, otherwise False.
        """
        try:
            with Image.open(input_path) as img:
                enhanced = ImageEnhance.Brightness(img).enhance(self.brightness_factor)
                enhanced = ImageEnhance.Contrast(enhanced).enhance(self.contrast_factor)
                enhanced = ImageEnhance.Color(enhanced).enhance(self.saturation_factor)
                enhanced.save(output_path, quality=95)

            return True

        except OSError as exc:
            print(f"Error processing {input_path}: {exc}")
            return False
