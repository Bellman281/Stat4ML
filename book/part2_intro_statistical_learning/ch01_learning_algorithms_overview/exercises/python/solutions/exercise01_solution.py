"""Chapter 1 (Part II) -- reference solution."""
import math


def simple_linear_regression_fit(xs, ys):
    n = len(xs)
    xbar = sum(xs) / n
    ybar = sum(ys) / n
    num = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    den = sum((x - xbar) ** 2 for x in xs)
    b1 = num / den
    b0 = ybar - b1 * xbar
    return b0, b1


def predict(xs, b0, b1):
    return [b0 + b1 * x for x in xs]


def mse(y_true, y_pred):
    n = len(y_true)
    return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / n


def kmeans_assign(points, centroids):
    assignments = []
    for (px, py) in points:
        dists = [math.sqrt((px - cx) ** 2 + (py - cy) ** 2) for (cx, cy) in centroids]
        assignments.append(dists.index(min(dists)))
    return assignments


def online_mean_update(old_mean, new_x, n):
    return old_mean + (new_x - old_mean) / n


def main():
    xs = [1.0, 2.0, 3.0, 4.0, 5.0]
    ys = [2.1, 3.9, 6.2, 7.8, 10.1]
    b0, b1 = simple_linear_regression_fit(xs, ys)
    preds = predict(xs, b0, b1)
    print(f"Fitted line: y = {b0:.3f} + {b1:.3f} x, MSE = {mse(ys, preds):.4f}")

    points = [(0.0, 0.0), (0.2, 0.1), (5.0, 5.0), (5.1, 4.9)]
    centroids = [(0.0, 0.0), (5.0, 5.0)]
    assignments = kmeans_assign(points, centroids)
    print("K-means assignments:", assignments)

    stream = [4.0, 6.0, 8.0, 2.0, 10.0]
    mean = stream[0]
    for n, x in enumerate(stream[1:], start=2):
        mean = online_mean_update(mean, x, n)
    print(f"Final running mean = {mean:.4f} (batch mean = {sum(stream)/len(stream):.4f})")


if __name__ == "__main__":
    main()
