from PIL import Image
import os

IMG_FILE = "data\\testSample\img_1.jpg"

path = os.path.join(os.getcwd(), IMG_FILE)

image = Image.open(path)

image.show()