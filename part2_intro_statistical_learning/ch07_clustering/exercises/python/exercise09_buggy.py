"""
Chapter 7 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (kpp_weight, silhouette). Fix one function at a time until
all tests pass. Do not edit run_tests().
"""
# level: research
import math


def kpp_weight(point, chosen):
    # BUG: k-means++ uses the distance to the NEAREST chosen centroid (min),
    # not the farthest (max) (ch07_text.tex Section 2, k-means++ seeding).
    return max((point[0] - c[0]) ** 2 + (point[1] - c[1]) ** 2 for c in chosen)


def is_core(point, data, eps, min_pts):
    count = 0
    for q in data:
        if math.hypot(point[0] - q[0], point[1] - q[1]) <= eps:
            count += 1
    return count >= min_pts


def silhouette(a, b):
    # BUG: the silhouette is (b - a) / max(a, b); this has the numerator
    # reversed (ch07_text.tex Section 3).
    return (a - b) / max(a, b)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = (got == expected) if isinstance(expected, bool) else abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    chosen = [[0, 0], [5, 5]]
    data = [[0, 0], [1, 0], [0, 1], [5, 5]]
    check("kpp_weight", kpp_weight([4, 4], chosen), 2.0)
    check("is_core", is_core([0, 0], data, 1.5, 3), True)
    check("silhouette", silhouette(2.0, 5.0), 0.6)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
