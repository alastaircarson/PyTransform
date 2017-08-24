from PIL import Image, ImageDraw
import json
from shapely.geometry import shape
from position_transform import Scale, Shift, Rotation, HorizontalFlip
from math import pi
from images2gif import writeGif


def main():
    # load GeoJSON file containing sectors
    with open('scotland.geojson', 'r') as f:
        js = json.load(f)

    # check each polygon to see if it contains the point
    overall_bounds = None
    for feature in js['features']:
        polygon = shape(feature['geometry'])
        overall_bounds = _merge_bounds(overall_bounds, polygon.bounds) if overall_bounds is not None else polygon.bounds
    print(overall_bounds)

    images = []

    for r in list(range(0, 20)):
        rot = r * 2 * pi / 20
        sc = 1 / ((21-r) * 0.1)

        # make a blank image
        img = Image.new('RGBA', (500, 500), (255, 255, 255, 0))

        transform = setup_transform(overall_bounds, 500, rot, sc)

        d = ImageDraw.Draw(img)

        for feature in js['features']:
            polygon = shape(feature['geometry'])
            transformed = []
            for point in polygon.exterior.coords:
                transformed.append(transform.transform(point))
            d.polygon(transformed, 0, 2)

        images.append(img)

    size = (500, 500)
    for im in images:
        im.thumbnail(size, Image.ANTIALIAS)

    filename = "rotation_and_scale.gif"
    writeGif(filename, images, duration=0.25, subRectangles=False)


def _merge_bounds(bounds_1, bounds_2):
    return (
        min(bounds_1[0], bounds_2[0]),
        min(bounds_1[1], bounds_2[1]),
        max(bounds_1[2], bounds_2[2]),
        max(bounds_1[3], bounds_2[3])
    )


def setup_transform(bounds, image_size, rotation, mod_scale):
    # Bounding Box Calculation
    centre_x = (bounds[0] + bounds[2])/2
    centre_y = (bounds[1] + bounds[3])/2
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]

    # Setup Transformation
    shift_to_zero = Shift(-centre_x, -centre_y)
    scale = Scale(image_size/max(width, height)*mod_scale)
    rotate = Rotation(rotation)
    flip = HorizontalFlip()
    shift_to_image_centre = Shift(image_size/2, image_size/2)
    return shift_to_image_centre.combine(flip).combine(rotate).combine(scale).combine(shift_to_zero)


if __name__ == "__main__":
    main()
