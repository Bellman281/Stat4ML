"""Reference solution for exercise03.py (Chapter 1, Exercise 3)."""
import math
import random


def independence_check(p_a, p_b, p_a_and_b, tol=1e-9):
    return abs(p_a_and_b - p_a * p_b) < tol


def intersection_with_complement(p_a, p_b_and_a):
    return p_a - p_b_and_a


def exponential_cdf(y):
    return 1.0 - math.exp(-y) if y >= 0 else 0.0


def probability_integral_transform_mean(n, seed=0):
    rng = random.Random(seed)
    total = 0.0
    for _ in range(n):
        u = max(rng.random(), 1e-12)
        x = -math.log(u)
        y = exponential_cdf(x)
        total += y
    return total / n


def main():
    print(f"independent (0.5, 0.4, 0.2): {independence_check(0.5, 0.4, 0.2)}  (expect True)")
    print(f"independent (0.5, 0.4, 0.3): {independence_check(0.5, 0.4, 0.3)}  (expect False)")

    print(f"P(A n B^c), A=0.5,B=0.4,AnB=0.3: {intersection_with_complement(0.5, 0.3)}  (expect 0.2)")

    print(f"exponential_cdf(0) = {exponential_cdf(0)}  (expect 0)")
    print(f"exponential_cdf(1) = {exponential_cdf(1):.4f}  (expect ~0.6321)")

    mean = probability_integral_transform_mean(200_000, seed=7)
    print(f"probability_integral_transform_mean = {mean:.4f}  (Uniform(0,1) mean is 0.5)")


if __name__ == "__main__":
    main()
