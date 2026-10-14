"""Chapter 6 -- reference solution (Proof)."""
# level: proof
import math


def sup_norm(v, u):
    return max(abs(a - b) for a, b in zip(v, u))


def geometric_bound(init_err, gamma, k):
    return init_err * gamma ** k


def num_iters_for_tol(init_err, gamma, tol):
    if init_err <= tol:
        return 0
    return max(0, math.ceil(math.log(tol / init_err) / math.log(gamma)))


def main():
    print("sup_norm          :", sup_norm([1.0, 2.0, 3.0], [1.0, 2.0, 5.0]))
    print("geometric_bound   :", geometric_bound(10.0, 0.9, 2))
    print("num_iters_for_tol :", num_iters_for_tol(1.0, 0.9, 0.01))


if __name__ == "__main__":
    main()
