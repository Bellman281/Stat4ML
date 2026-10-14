"""Chapter 10 -- reference solution (Core)."""
# level: core
import math


def nonconformity(y, pred):
    return abs(y - pred)


def quantile_rank(n, alpha):
    return math.ceil((n + 1) * (1 - alpha))


def coverage(ys, preds, q):
    return sum(1 for y, p in zip(ys, preds) if abs(y - p) <= q) / len(ys)


def main():
    print("nonconformity :", nonconformity(3.0, 2.5))
    print("quantile_rank :", quantile_rank(99, 0.1))
    print("coverage      :", coverage([1.0, 2.0, 3.0], [1.0, 2.0, 5.0], 1.0))


if __name__ == "__main__":
    main()
