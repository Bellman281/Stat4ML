"""Reference solution for exercise02.py (Chapter 1, Exercise 2)."""
import math
import random


def _choose3(x):
    return {0: 1, 1: 3, 2: 3, 3: 1}.get(x, 0)


def pmf_three_coins(x):
    return _choose3(x) * (0.5 ** 3)


def cdf_three_coins(x):
    k = math.floor(x)
    return sum(pmf_three_coins(i) for i in range(4) if i <= k)


def inverse_transform_sample(u):
    return -math.log(u)


def exponential_pdf(y):
    return math.exp(-y) if y >= 0 else 0.0


def main():
    total = sum(pmf_three_coins(x) for x in range(4))
    print(f"sum of pmf over x=0..3: {total}  (should be 1.0)")

    print(f"F_X(2.5) = {cdf_three_coins(2.5)}  (should be 7/8 = 0.875)")
    print(f"F_X(-1) = {cdf_three_coins(-1)}, F_X(3.5) = {cdf_three_coins(3.5)}")

    rng = random.Random(7)
    n = 200_000
    samples = [inverse_transform_sample(max(rng.random(), 1e-12)) for _ in range(n)]
    mean = sum(samples) / n
    print(f"mean of {n} inverse-transform samples: {mean:.4f}  (Exponential(1) mean is 1.0)")


if __name__ == "__main__":
    main()
