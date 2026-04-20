import qrcode
import qrcode.image.svg as svg
import os

factory = svg.SvgPathImage  # smoother paths

img = qrcode.make("https://jolinks.netlify.app/", image_factory=factory)
img.save("my_qr_code.svg")
print(os.getcwd())