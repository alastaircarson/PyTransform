from math import sin, cos


class PositionTransform:
    matrix = None

    def __init__(self):
        self.identity()

    def identity(self):
        self.matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    def print(self):
        print(self.matrix)

    def transform(self, coord):
        transformed = (
            coord[0] * self.matrix[0][0] + coord[1] * self.matrix[0][1] + self.matrix[0][2],
            coord[0] * self.matrix[1][0] + coord[1] * self.matrix[1][1] + self.matrix[1][2])
        return transformed

    def combine(self, transform):
        result = PositionTransform()

        result.matrix[0][0] = self.matrix[0][0] * transform.matrix[0][0] + self.matrix[0][1] * transform.matrix[1][0] + \
                              self.matrix[0][2] * transform.matrix[2][0]
        result.matrix[0][1] = self.matrix[0][0] * transform.matrix[0][1] + self.matrix[0][1] * transform.matrix[1][1] + \
                              self.matrix[0][2] * transform.matrix[2][1]
        result.matrix[0][2] = self.matrix[0][0] * transform.matrix[0][2] + self.matrix[0][1] * transform.matrix[1][2] + \
                              self.matrix[0][2] * transform.matrix[2][2]
        result.matrix[1][0] = self.matrix[1][0] * transform.matrix[0][0] + self.matrix[1][1] * transform.matrix[1][0] + \
                              self.matrix[1][2] * transform.matrix[2][0]
        result.matrix[1][1] = self.matrix[1][0] * transform.matrix[0][1] + self.matrix[1][1] * transform.matrix[1][1] + \
                              self.matrix[1][2] * transform.matrix[2][1]
        result.matrix[1][2] = self.matrix[1][0] * transform.matrix[0][2] + self.matrix[1][1] * transform.matrix[1][2] + \
                              self.matrix[1][2] * transform.matrix[2][2]
        result.matrix[2][0] = self.matrix[2][0] * transform.matrix[0][0] + self.matrix[2][1] * transform.matrix[1][0] + \
                              self.matrix[2][2] * transform.matrix[2][0]
        result.matrix[2][1] = self.matrix[2][0] * transform.matrix[0][1] + self.matrix[2][1] * transform.matrix[1][1] + \
                              self.matrix[2][2] * transform.matrix[2][1]
        result.matrix[2][2] = self.matrix[2][0] * transform.matrix[0][2] + self.matrix[2][1] * transform.matrix[1][2] + \
                              self.matrix[2][2] * transform.matrix[2][2]
        return result


class Shift(PositionTransform):
    def __init__(self, x_offset, y_offset):
        PositionTransform.__init__(self)
        self.matrix[0][2] = x_offset
        self.matrix[1][2] = y_offset


class Scale(PositionTransform):
    def __init__(self, scale):
        PositionTransform.__init__(self)
        self.matrix[0][0] = scale
        self.matrix[1][1] = scale


class Rotation(PositionTransform):
    def __init__(self, angle):
        PositionTransform.__init__(self)
        self.matrix[0][0] = cos(angle)
        self.matrix[0][1] = -sin(angle)
        self.matrix[1][0] = sin(angle)
        self.matrix[1][1] = cos(angle)


class HorizontalFlip(PositionTransform):
    def __init__(self):
        PositionTransform.__init__(self)
        self.matrix[1][1] = -1
