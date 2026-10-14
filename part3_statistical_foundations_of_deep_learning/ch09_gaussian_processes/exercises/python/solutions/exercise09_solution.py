"""Chapter 9 -- reference solution (Core)."""
# level: core
import math


def rbf_kernel(x1, x2, length):
    return math.exp(-(x1 - x2) ** 2 / (2 * length ** 2))


def kernel_vector(x, xs, length):
    return [rbf_kernel(x, xi, length) for xi in xs]


def linear_kernel(x1, x2):
    return x1 * x2


def main():
    print("rbf_kernel(0,0) :", rbf_kernel(0.0, 0.0, 1.0))
    print("rbf_kernel(0,1) :", rbf_kernel(0.0, 1.0, 1.0))
    print("kernel_vector   :", kernel_vector(0.0, [0.0, 1.0, 2.0], 1.0))
    print("linear_kernel   :", linear_kernel(2.0, 3.0))


if __name__ == "__main__":
    main()
