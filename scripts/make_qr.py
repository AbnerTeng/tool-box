import qrcode

class QRCodeGenerator:
    def __init__(self, content: str):
        self.content = content
        self.qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=0
        )


    def get_qrcode(self):
        self.qr.add_data(self.content)
        self.qr.make(fit=True)
        image = self.qr.make_image(fill_color="black", back_color="white")
        return image