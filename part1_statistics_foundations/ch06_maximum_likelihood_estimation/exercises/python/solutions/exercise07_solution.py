"""Chapter 6 -- reference solution (Proof)."""
# level: proof
import math
import random


def score_bernoulli(p, data):
    return sum(x / p - (1 - x) / (1 - p) for x in data)


def fisher_information_bernoulli(p, n):
    return n / (p * (1 - p))


def cramer_rao_lower_bound(p, n):
    return p * (1 - p) / n


def mle_variance_sim(p, n, reps, seed=0):
    rng = random.Random(seed)
    est = []
    for _ in range(reps):
        ones = sum(1 for _ in range(n) if rng.random() < p)
        est.append(ones / n)
    m = sum(est) / reps
    return sum((e - m) ** 2 for e in est) / reps


def main():
    data = [1] * 15 + [0] * 35
    print(f"score at MLE p=0.3 : {score_bernoulli(0.3, data):.6f}")
    print(f"Fisher info(0.3,50): {fisher_information_bernoulli(0.3, 50):.4f}")
    print(f"CRLB(0.3,50)       : {cramer_rao_lower_bound(0.3, 50):.6f}")
    print(f"sim var of MLE     : {mle_variance_sim(0.3, 50, 20000, seed=0):.6f}")


if __name__ == "__main__":
    main()
