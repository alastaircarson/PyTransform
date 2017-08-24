from PIL import Image, ImageDraw
from io import BytesIO

# make a blank image for the text, initialized to transparent text color
img = Image.new('RGBA', (500, 500), (255, 255, 255, 0))

d = ImageDraw.Draw(img)
d.line([(100, 100), (100, 200)], 0, 2)

with BytesIO() as img_bytes:
    img.save(img_bytes, 'GIF')
    print(img_bytes.getbuffer().nbytes)
    img_bytes.seek(0)
    with open('test.gif', 'wb') as fp:
        fp.write(img_bytes.read())

