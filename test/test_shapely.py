import json
from shapely.geometry import shape


def main():

    # load GeoJSON file containing sectors
    with open('Letters.geojson', 'r') as f:
        js = json.load(f)

    # check each polygon to see if it contains the point
    overall_bounds = None
    for feature in js['features']:
        line = shape(feature['geometry'])
        overall_bounds = _merge_bounds(overall_bounds, line.bounds) if overall_bounds is not None else line.bounds
    print(overall_bounds)

    for feature in js['features']:
        line = shape(feature['geometry'])
        for point in line.coords:
            print(point)


def _merge_bounds(bounds_1, bounds_2):
    return (
        min(bounds_1[0], bounds_2[0]),
        min(bounds_1[1], bounds_2[1]),
        min(bounds_1[2], bounds_2[2]),
        min(bounds_1[3], bounds_2[3])
    )


if __name__ == "__main__":
    main()
