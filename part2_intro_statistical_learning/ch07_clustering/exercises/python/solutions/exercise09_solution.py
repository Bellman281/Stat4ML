"""Chapter 7 -- reference solution (Research)."""
# level: research
import math


def kpp_weight(point, chosen):
    return min((point[0] - c[0]) ** 2 + (point[1] - c[1]) ** 2 for c in chosen)


def is_core(point, data, eps, min_pts):
    count = sum(1 for q in data if math.hypot(point[0] - q[0], point[1] - q[1]) <= eps)
    return count >= min_pts


def silhouette(a, b):
    return (b - a) / max(a, b)


def main():
    chosen = [[0, 0], [5, 5]]
    data = [[0, 0], [1, 0], [0, 1], [5, 5]]
    print("kpp_weight :", kpp_weight([4, 4], chosen))
    print("is_core    :", is_core([0, 0], data, 1.5, 3))
    print("silhouette :", silhouette(2.0, 5.0))


if __name__ == "__main__":
    main()
