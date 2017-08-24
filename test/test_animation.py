from images2gif import writeGif
from PIL import Image
from io import BytesIO

file_names = ['test1.gif', 'test2.gif']
file_bytes = []
for fn in file_names:
    file_bytes.append(BytesIO(open(fn, "rb").read()))

images = [Image.open(fb) for fb in file_bytes]

size = (500, 500)
for im in images:
    im.thumbnail(size, Image.ANTIALIAS)

filename = "testa.gif"
writeGif(filename, images, duration=0.5, subRectangles=False)
