"""Chapter 2 -- reference solution (Core)."""
# level: core
import math


def mse(preds, targets):
    return sum((p - t) ** 2 for p, t in zip(preds, targets)) / len(targets)


def bernoulli_nll(p, y):
    return -(y * math.log(p) + (1 - y) * math.log(1 - p))


def gaussian_nll(mu, ys, sigma):
    n = len(ys)
    const = n / 2 * math.log(2 * math.pi * sigma ** 2)
    return const + sum((y - mu) ** 2 for y in ys) / (2 * sigma ** 2)


def main():
    print("mse           :", mse([1, 2, 3], [1, 2, 5]))
    print("bernoulli_nll :", bernoulli_nll(0.8, 1))
    print("gaussian_nll  :", gaussian_nll(0.0, [1.0, -1.0], 2.0))


if __name__ == "__main__":
    main()
