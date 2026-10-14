"""Chapter 10 -- reference solution (Proof)."""
# level: proof
import math


def conformal_q(cal_scores, alpha):
    n = len(cal_scores)
    k = math.ceil((n + 1) * (1 - alpha))
    if k > n:
        return math.inf
    return sorted(cal_scores)[k - 1]


def empirical_coverage(test_scores, q):
    return sum(1 for s in test_scores if s <= q) / len(test_scores)


def guarantee_holds(cov, alpha):
    return cov >= 1 - alpha - 1e-9


def main():
    cal = [0.2, 0.4, 0.6, 0.8, 1.0]
    q = conformal_q(cal, 0.2)
    print("conformal_q       :", q)
    cov = empirical_coverage([0.5, 0.9, 1.5, 0.1, 0.7], q)
    print("empirical_coverage:", cov)
    print("guarantee_holds   :", guarantee_holds(cov, 0.2))


if __name__ == "__main__":
    main()
