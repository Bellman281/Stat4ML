"""Chapter 3 -- reference solution (Core)."""
# level: core
import math


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def logistic_proba(w, x):
    return sigmoid(sum(wi * xi for wi, xi in zip(w, x)))


def cross_entropy(y, p):
    return -(y * math.log(p) + (1 - y) * math.log(1 - p))


def classify(p, threshold=0.5):
    return 1 if p >= threshold else 0


def main():
    print("sigmoid(0)        :", sigmoid(0.0))
    print("proba([0,1,1],.)  :", logistic_proba([0, 1, 1], [1, 2, -2]))
    print("cross_entropy     :", cross_entropy(1, 0.5))
    print("classify(0.7)     :", classify(0.7))


if __name__ == "__main__":
    main()
