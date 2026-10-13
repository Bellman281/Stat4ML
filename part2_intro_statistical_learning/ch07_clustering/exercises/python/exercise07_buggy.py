"""
Chapter 7 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (nearest, centroid). Fix one function at a time until all
tests pass. Do not edit run_tests().
"""
# level: core


def sq_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def nearest(point, centroids):
    # BUG: the nearest centroid minimises the distance, so this should be
    # min(...), not max(...) (ch07_text.tex Section 2, assignment step).
    return max(range(len(centroids)), key=lambda k: sq_dist(point, centroids[k]))


def centroid(points):
    n = len(points)
    # BUG: the y-coordinate averages points[i][1], not points[i][0].
    return [sum(p[0] for p in points) / n, sum(p[0] for p in points) / n]


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        if isinstance(expected, list):
            ok = all(abs(g - e) < tol for g, e in zip(got, expected)) and len(got) == len(expected)
        else:
            ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    cs = [[0.0, 0.0], [5.0, 5.0]]
    check("sq_dist", sq_dist([0, 0], [3, 4]), 25.0)
    check("nearest", nearest([4.0, 4.0], cs), 1)
    check("centroid", centroid([[0, 0], [2, 0], [1, 6]]), [1.0, 2.0])

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
