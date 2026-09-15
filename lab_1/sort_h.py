class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance_squared(point):
    return point.x * point.x + point.y * point.y


def sort_points(points):
    n = len(points)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if distance_squared(points[j]) < distance_squared(points[min_index]):
                min_index = j

        points[i], points[min_index] = points[min_index], points[i]


n = int(input())

points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

sort_points(points)

for point in points:
    print(point.x, point.y)