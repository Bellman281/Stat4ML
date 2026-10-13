"""
Chapter 7 exercise -- k-means primitives (Core tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch07_text.tex Sections 1-2. Points are
2D lists [x, y]. These three primitives are everything Lloyd's algorithm
needs: a distance, a nearest-centroid lookup, and a mean.

Run with:  python3 exercise07.py
Reference solution: solutions/exercise07_solution.py
"""
# level: core


def sq_dist(a, b):
    """Squared Euclidean distance between 2D points a=[x,y] and b=[x,y]."""
    raise NotImplementedError("TODO: sq_dist")


def nearest(point, centroids):
    """Index of the centroid in `centroids` closest to `point`."""
    raise NotImplementedError("TODO: nearest")


def centroid(points):
    """Mean of a list of 2D points -> [mean_x, mean_y]."""
    raise NotImplementedError("TODO: centroid")


def main():
    cs = [[0.0, 0.0], [5.0, 5.0]]
    print("sq_dist :", sq_dist([0, 0], [3, 4]))
    print("nearest :", nearest([4.0, 4.0], cs))
    print("centroid:", centroid([[0, 0], [2, 0], [1, 6]]))


if __name__ == "__main__":
    main()
