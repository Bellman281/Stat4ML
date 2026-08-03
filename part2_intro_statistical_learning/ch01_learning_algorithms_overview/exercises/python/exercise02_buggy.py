"""
Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Python edition), Exercise 2
Part II: Introduction to Statistical Learning

Three deliberate bugs are hiding below (in euclidean_dist2,
kmeans_assign, and kmeans_update_centroids). Run this file, read the
first failing assertion, fix ONLY that function, and re-run -- repeat
until you see "All tests passed!". Do not edit run_tests().
"""


def euclidean_dist2(p, q):
    # BUG: subtracts instead of adds the two squared terms -- can even
    # be negative, which is never a valid squared distance.
    return (p[0] - q[0]) ** 2 - (p[1] - q[1]) ** 2


def kmeans_assign(points, centroids):
    # BUG: uses argmax instead of argmin -- assigns every point to the
    # FARTHEST centroid instead of the nearest one.
    assignments = []
    for p in points:
        dists = [euclidean_dist2(p, c) for c in centroids]
        assignments.append(dists.index(max(dists)))
    return assignments


def kmeans_update_centroids(points, assignments, k):
    # BUG: ignores `assignments` entirely -- every centroid becomes the
    # mean of ALL points, not just the ones assigned to it.
    n = len(points)
    mean_x = sum(p[0] for p in points) / n
    mean_y = sum(p[1] for p in points) / n
    return [(mean_x, mean_y) for _ in range(k)]


def kmeans_iterate(points, centroids, n_iters):
    # Correct (not part of this exercise).
    for _ in range(n_iters):
        assignments = kmeans_assign(points, centroids)
        centroids = kmeans_update_centroids(points, assignments, len(centroids))
    return centroids


# --------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# --------------------------------------------------------------------------
def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-6):
        if isinstance(expected, list) and expected and isinstance(expected[0], tuple):
            ok = all(abs(g[0] - e[0]) < tol and abs(g[1] - e[1]) < tol for g, e in zip(got, expected))
        elif isinstance(expected, (int, float)):
            ok = abs(got - expected) < tol
        else:
            ok = got == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("euclidean_dist2((0,0),(3,4))", euclidean_dist2((0, 0), (3, 4)), 25)

    points = [(0.0, 0.0), (0.2, 0.1), (5.0, 5.0), (5.1, 4.9)]
    centroids = [(1.0, 1.0), (4.0, 4.0)]
    assignments = kmeans_assign(points, centroids)
    check("kmeans_assign", assignments, [0, 0, 1, 1])

    updated = kmeans_update_centroids(points, [0, 0, 1, 1], 2)
    check("kmeans_update_centroids", updated, [(0.1, 0.05), (5.05, 4.95)])

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
