"""Chapter 7 -- reference solution (Core)."""
# level: core


def sq_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def nearest(point, centroids):
    return min(range(len(centroids)), key=lambda k: sq_dist(point, centroids[k]))


def centroid(points):
    n = len(points)
    return [sum(p[0] for p in points) / n, sum(p[1] for p in points) / n]


def main():
    cs = [[0.0, 0.0], [5.0, 5.0]]
    print("sq_dist :", sq_dist([0, 0], [3, 4]))
    print("nearest :", nearest([4.0, 4.0], cs))
    print("centroid:", centroid([[0, 0], [2, 0], [1, 6]]))


if __name__ == "__main__":
    main()
