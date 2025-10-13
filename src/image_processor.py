import cv2
import numpy as np
from PIL import Image, ImageEnhance

# image enhancement processor class
class ImageEnhancer:
    def __init__(self):
        # default enhancement values
        self.brightness_factor = 1.27
        self.contrast_factor = 1.1
        self.saturation_factor = 1.05

    def process_image(self, input_path, output_path):
        # process single image with enhancement settings
        try:
            img = Image.open(input_path)
            
            # apply brightness enhancement
            enhancer = ImageEnhance.Brightness(img)
            enhanced = enhancer.enhance(self.brightness_factor)
            
            # apply contrast enhancement
            contrast = ImageEnhance.Contrast(enhanced)
            enhanced = contrast.enhance(self.contrast_factor)
            
            # apply saturation enhancement
            saturation = ImageEnhance.Color(enhanced)
            enhanced = saturation.enhance(self.saturation_factor)
            
            # save enhanced image with high quality
            enhanced.save(output_path, quality=95)
            
            return True
            
        except Exception as e:
            print(f"Error processing {input_path}: {str(e)}")
            return False
