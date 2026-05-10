from PIL import Image, ImageEnhance


class ImageEnhancer:
    """Apply a consistent brightness, contrast, and saturation pass to images."""

    def __init__(self):
        self.brightness_factor = 1.27
        self.contrast_factor = 1.1
        self.saturation_factor = 1.05

    def process_image(self, input_path, output_path):
        """Enhance a single image and save it to the requested output path."""
        try:
            with Image.open(input_path) as img:
                enhanced = ImageEnhance.Brightness(img).enhance(self.brightness_factor)
                enhanced = ImageEnhance.Contrast(enhanced).enhance(self.contrast_factor)
                enhanced = ImageEnhance.Color(enhanced).enhance(self.saturation_factor)
                enhanced.save(output_path, quality=95)

            return True

        except Exception as e:
            print(f"Error processing {input_path}: {str(e)}")
            return False
