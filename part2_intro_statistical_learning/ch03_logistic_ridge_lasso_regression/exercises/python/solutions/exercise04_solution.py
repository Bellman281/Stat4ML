"""Chapter 3 -- reference solution (Proof)."""
# level: proof
import math


def ridge_estimator_1d(x, y, lam):
    xbar = sum(x) / len(x); ybar = sum(y) / len(y)
    sxy = sum((xi - xbar) * (yi - ybar) for xi, yi in zip(x, y))
    sxx = sum((xi - xbar) ** 2 for xi in x)
    return sxy / (sxx + lam)


def soft_threshold(z, lam):
    if z > lam: return z - lam
    if z < -lam: return z + lam
    return 0.0


def sigmoid_prime(z):
    s = 1.0 / (1.0 + math.exp(-z))
    return s * (1 - s)


def main():
    x = [1, 2, 3]; y = [2, 4, 6]
    print("ridge (lam=2)     :", ridge_estimator_1d(x, y, 2.0))
    print("soft_threshold    :", soft_threshold(-2.0, 1.0))
    print("sigmoid_prime(0)  :", sigmoid_prime(0.0))


if __name__ == "__main__":
    main()
