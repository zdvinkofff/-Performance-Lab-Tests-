import sys
import math


def check_point_position(circle_file, points_file):
    with open(circle_file) as cf:
        x0, y0 = map(float, cf.readline().split())
        r = float(cf.readline())

    with open(points_file) as pf:
        points = [list(map(float, line.split())) for line in pf]

    results = []
    for x, y in points:
        distance = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if distance < r:
            results.append(1)
        elif distance == r:
            results.append(0)
        else:
            results.append(2)

    for result in results:
        print(result)


if __name__ == "__main__":
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    check_point_position(circle_file, points_file)
