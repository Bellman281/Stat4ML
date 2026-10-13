"""Chapter 5 -- reference solution (Core)."""
# level: core
def center(v):
    m = sum(v) / len(v)
    return [vi - m for vi in v]


def variance(v):
    m = sum(v) / len(v)
    return sum((vi - m) ** 2 for vi in v) / len(v)


def covariance(x, y):
    xbar = sum(x) / len(x); ybar = sum(y) / len(y)
    return sum((xi - xbar) * (yi - ybar) for xi, yi in zip(x, y)) / len(x)


def variance_explained_ratio(eigvals):
    total = sum(eigvals)
    return [e / total for e in eigvals]


def main():
    print("center      :", center([1, 2, 3]))
    print("variance    :", variance([1, 2, 3]))
    print("covariance  :", covariance([1, 2, 3], [1, 2, 3]))
    print("var ratio   :", variance_explained_ratio([3, 1]))


if __name__ == "__main__":
    main()
