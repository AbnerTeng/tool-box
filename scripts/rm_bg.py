from rembg import remove
from PIL import Image

class Remover:
    def __init__(self, input_path: str):
        self.input_path = input_path


    def remove_bg(self):
        """
        Remove the figure background
        """
        img = Image.open(self.input_path)
        output = remove(img)
        return output
