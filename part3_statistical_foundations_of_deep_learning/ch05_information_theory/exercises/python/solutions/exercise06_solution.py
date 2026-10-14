"""Chapter 5 -- reference solution (Proof)."""
# level: proof
import math


def _entropy(p):
    return -sum(pi * math.log(pi) for pi in p)


def _cross_entropy(p, q):
    return -sum(pi * math.log(qi) for pi, qi in zip(p, q))


def _kl(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q))


def identity_residual(p, q):
    return _cross_entropy(p, q) - _entropy(p) - _kl(p, q)


def kl_is_nonneg(p, q):
    return _kl(p, q) >= -1e-12


def log_bound_gap(t):
    return (t - 1) - math.log(t)


def main():
    p = [0.2, 0.3, 0.5]; q = [0.3, 0.4, 0.3]
    print("identity_residual:", identity_residual(p, q))
    print("kl_is_nonneg     :", kl_is_nonneg(p, q))
    print("log_bound_gap(2) :", log_bound_gap(2.0))
    print("log_bound_gap(1) :", log_bound_gap(1.0))


if __name__ == "__main__":
    main()
