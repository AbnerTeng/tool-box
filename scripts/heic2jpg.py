from PIL import Image
from pillow_heif import register_heif_opener

class Converter:
    def __init__(self, input_path: str) -> None:
        self.input_path = input_path
        register_heif_opener()

    def heic2jpg(self) -> Image:
        try:
            img = Image.open(self.input_path)
            img = img.convert("RGB")
            return img
        except Exception as e:
            print(f"Error converting HEIC to JPG: {e}")      
        