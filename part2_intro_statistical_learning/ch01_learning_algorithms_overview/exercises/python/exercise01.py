"""
Chapter 1 exercise -- Learning Algorithms Overview
Part II: Introduction to Statistical Learning

HOMEWORK: implement one small, working example of each of the three
learning paradigms most fully developed later in Part II:
  - supervised learning:   closed-form simple linear regression (least squares)
  - unsupervised learning: a single K-means assignment step
  - online learning:       an incremental (running) mean update

Only Python's standard library is required. Run with:
    python3 exercise01.py
Reference solution: solutions/exercise01_solution.py
"""
import math


def simple_linear_regression_fit(xs, ys):
    """Fit y = b0 + b1*x by ordinary least squares (closed form), for a
    single predictor. Return (b0, b1).

    Recall the least-squares slope/intercept:
        b1 = sum((x_i - xbar)*(y_i - ybar)) / sum((x_i - xbar)^2)
        b0 = ybar - b1 * xbar
    """
    # TODO
    raise NotImplementedError("TODO: simple_linear_regression_fit")


def predict(xs, b0, b1):
    """Return [b0 + b1*x for x in xs]."""
    # TODO
    raise NotImplementedError("TODO: predict")


def mse(y_true, y_pred):
    """Mean squared error: average of (y_true_i - y_pred_i)^2."""
    # TODO
    raise NotImplementedError("TODO: mse")


def kmeans_assign(points, centroids):
    """Unsupervised learning step. `points` and `centroids` are lists of
    (x, y) tuples. For each point, return the index of the nearest
    centroid (Euclidean distance), as a list of ints of len(points)."""
    # TODO: for each point, compute Euclidean distance to every centroid
    # and keep the index of the minimum.
    raise NotImplementedError("TODO: kmeans_assign")


def online_mean_update(old_mean, new_x, n):
    """Online (incremental) learning step. Given the mean of the first
    n-1 observations (`old_mean`) and a new observation `new_x` that
    brings the count to `n`, return the updated mean WITHOUT re-averaging
    the full history:
        new_mean = old_mean + (new_x - old_mean) / n
    """
    # TODO
    raise NotImplementedError("TODO: online_mean_update")


def main():
    # Supervised: fit a line to (advertising budget, sales)-like toy data.
    xs = [1.0, 2.0, 3.0, 4.0, 5.0]
    ys = [2.1, 3.9, 6.2, 7.8, 10.1]
    b0, b1 = simple_linear_regression_fit(xs, ys)
    preds = predict(xs, b0, b1)
    print(f"Fitted line: y = {b0:.3f} + {b1:.3f} x, MSE = {mse(ys, preds):.4f}")

    # Unsupervised: assign points to 2 clusters.
    points = [(0.0, 0.0), (0.2, 0.1), (5.0, 5.0), (5.1, 4.9)]
    centroids = [(0.0, 0.0), (5.0, 5.0)]
    assignments = kmeans_assign(points, centroids)
    print("K-means assignments:", assignments)

    # Online learning: track a running mean without storing history.
    stream = [4.0, 6.0, 8.0, 2.0, 10.0]
    mean = stream[0]
    for n, x in enumerate(stream[1:], start=2):
        mean = online_mean_update(mean, x, n)
    print(f"Final running mean = {mean:.4f} (batch mean = {sum(stream)/len(stream):.4f})")


if __name__ == "__main__":
    main()
