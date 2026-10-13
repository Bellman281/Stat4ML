"""
Chapter 7 exercise -- seeding, density, and validity (Research tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch07_text.tex Sections 2-3. Three ideas
that go beyond plain Lloyd:
  - kpp_weight : the k-means++ seeding weight D(x)^2 = squared distance to the
                 nearest already-chosen centroid.
  - is_core    : DBSCAN's core-point test at scale (eps, min_pts).
  - silhouette : the silhouette score of a point, (b - a) / max(a, b).

Points are 2D lists [x, y]. Run with:  python3 exercise09.py
Reference solution: solutions/exercise09_solution.py
"""
# level: research
import math


def kpp_weight(point, chosen):
    """k-means++ weight: squared distance from `point` to the NEAREST centroid
    in the non-empty list `chosen`."""
    raise NotImplementedError("TODO: kpp_weight")


def is_core(point, data, eps, min_pts):
    """DBSCAN core point: True iff at least `min_pts` points of `data` lie
    within Euclidean distance `eps` of `point` (counting point itself)."""
    raise NotImplementedError("TODO: is_core")


def silhouette(a, b):
    """Silhouette score for one point: a = mean distance to its own cluster,
    b = mean distance to the nearest other cluster.  (b - a) / max(a, b)."""
    raise NotImplementedError("TODO: silhouette")


def main():
    chosen = [[0, 0], [5, 5]]
    data = [[0, 0], [1, 0], [0, 1], [5, 5]]
    print("kpp_weight :", kpp_weight([4, 4], chosen))
    print("is_core    :", is_core([0, 0], data, 1.5, 3))
    print("silhouette :", silhouette(2.0, 5.0))


if __name__ == "__main__":
    main()
