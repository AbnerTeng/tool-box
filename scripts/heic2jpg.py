"""
Converter
"""
from PIL import Image
from pillow_heif import register_heif_opener

class Converter:
    """
    Convert HEIC to JPG
    """
    def __init__(self, input_path: str) -> None:
        self.input_path = input_path
        register_heif_opener()

    def heic2jpg(self) -> Image:
        """
        main function to convert HEIC to JPG
        """
        try:
            img = Image.open(self.input_path)
            img = img.convert("RGB")
            return img

        except ValueError:
            print(f"Error converting HEIC to JPG: {self.input_path}")
