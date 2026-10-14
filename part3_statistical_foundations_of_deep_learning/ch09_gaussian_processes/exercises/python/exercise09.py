"""
Chapter 9 exercise -- kernels (Core tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch09_text.tex Section 1.
  - rbf_kernel    : exp( -(x1 - x2)^2 / (2 * length^2) ).
  - kernel_vector : [ rbf_kernel(x, xi, length) for xi in xs ].
  - linear_kernel : x1 * x2.

Run with:  python3 exercise09.py
Reference solution: solutions/exercise09_solution.py
"""
# level: core
import math


def rbf_kernel(x1, x2, length):
    """Squared-exponential kernel exp(-(x1-x2)^2 / (2 length^2))."""
    raise NotImplementedError("TODO: rbf_kernel")


def kernel_vector(x, xs, length):
    """RBF kernel of x against every point in xs (a list)."""
    raise NotImplementedError("TODO: kernel_vector")


def linear_kernel(x1, x2):
    """Linear kernel x1 * x2."""
    raise NotImplementedError("TODO: linear_kernel")


def main():
    print("rbf_kernel(0,0) :", rbf_kernel(0.0, 0.0, 1.0))
    print("rbf_kernel(0,1) :", rbf_kernel(0.0, 1.0, 1.0))
    print("kernel_vector   :", kernel_vector(0.0, [0.0, 1.0, 2.0], 1.0))
    print("linear_kernel   :", linear_kernel(2.0, 3.0))


if __name__ == "__main__":
    main()
