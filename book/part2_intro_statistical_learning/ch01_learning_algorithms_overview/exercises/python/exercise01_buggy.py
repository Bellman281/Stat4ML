"""
Chapter 1 (Part II) -- RUSTLINGS-STYLE EXERCISE (Python edition)

Four deliberate bugs are hiding below (in simple_linear_regression_fit,
predict, mse, and kmeans_assign). Run this file, read the first failing
assertion, fix ONLY that function, and re-run -- repeat until you see
"All tests passed!". Do not edit run_tests().
"""
import math


def simple_linear_regression_fit(xs, ys):
    # BUG: uses raw sums instead of centering around the means first, i.e.
    # computes b1 = sum(x*y) / sum(x*x) instead of the covariance-based
    # formula. This silently gives the wrong line whenever xbar != 0.
    n = len(xs)
    num = sum(x * y for x, y in zip(xs, ys))
    den = sum(x * x for x in xs)
    b1 = num / den
    ybar = sum(ys) / n
    xbar = sum(xs) / n
    b0 = ybar - b1 * xbar
    return b0, b1


def predict(xs, b0, b1):
    # BUG: forgets the intercept term entirely.
    return [b1 * x for x in xs]


def mse(y_true, y_pred):
    # BUG: computes mean ABSOLUTE error, not mean SQUARED error.
    n = len(y_true)
    return sum(abs(yt - yp) for yt, yp in zip(y_true, y_pred)) / n


def kmeans_assign(points, centroids):
    # BUG: only compares the x-coordinate, ignoring y entirely -- wrong
    # whenever clusters differ in the y dimension.
    assignments = []
    for (px, py) in points:
        dists = [abs(px - cx) for (cx, cy) in centroids]
        assignments.append(dists.index(min(dists)))
    return assignments


def online_mean_update(old_mean, new_x, n):
    # Correct.
    return old_mean + (new_x - old_mean) / n


# --------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# --------------------------------------------------------------------------
def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-6):
        if isinstance(expected, (list, tuple)):
            ok = len(got) == len(expected) and all(
                (abs(g - e) < tol if isinstance(e, float) else g == e)
                for g, e in zip(got, expected)
            )
        else:
            ok = abs(got - expected) < tol if isinstance(expected, float) else got == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    # y = 1 + 2x exactly, but NOT centered at x=0 (xbar=3 != 0), which is
    # exactly the case the buggy fit formula gets wrong.
    xs = [1.0, 2.0, 3.0, 4.0, 5.0]
    ys = [3.0, 5.0, 7.0, 9.0, 11.0]
    b0, b1 = simple_linear_regression_fit(xs, ys)
    check("simple_linear_regression_fit intercept", round(b0, 4), 1.0)
    check("simple_linear_regression_fit slope", round(b1, 4), 2.0)

    preds = predict([0.0, 1.0, 2.0], b0=1.0, b1=2.0)
    check("predict([0,1,2], b0=1, b1=2)", preds, [1.0, 3.0, 5.0])

    check("mse([1,2,3], [1,2,5])", mse([1, 2, 3], [1, 2, 5]), 4 / 3)

    points = [(0.0, 0.0), (0.2, 0.1), (0.0, 5.0), (0.1, 5.1)]
    centroids = [(0.0, 0.0), (0.0, 5.0)]
    # Points 0,1 are near centroid 0; points 2,3 are near centroid 1 --
    # but they all have small |x|, so an x-only distance would confuse them.
    check("kmeans_assign (needs both coordinates)",
          kmeans_assign(points, centroids), [0, 0, 1, 1])

    check("online_mean_update", round(online_mean_update(5.0, 15.0, 2), 4), 10.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
