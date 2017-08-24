from position_transform import Scale, Shift, Rotation, HorizontalFlip
from math import pi


def main():

    scale = Scale(1/500)
    shift = Shift(-300000, -500000)
    rotation = Rotation(pi/2)
    flip = HorizontalFlip()

    combined = scale.combine(shift).combine(rotation).combine(flip)
    combined.print()

    in_coord = (550000, 650000)
    out_coord = combined.transform(in_coord)
    print(out_coord)


if __name__ == "__main__":
    main()
