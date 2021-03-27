def getSurroundRect(points):
    up = 0
    down = 480
    left = 640
    right = 0
    for first in points:
        for third in first:
            # for third in second:
            if third[0] > up:
                up = third[0]
            if third[0] < down:
                down = third[0]
            if third[1] < left:
                left = third[1]
            if third[1] > right:
                right = third[1]
    # print("left", left)
    # print("right", right)
    # print("up", up)
    # print("down", down)
    width = right - left
    height = up - down
    point = [down, left]
    return [point, width, height]


def generatePoints(width, height):
    pts = []
    for i in range(width):
        for j in range(height):
            pts.append([[j, i]])
    return pts
