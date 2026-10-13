"""Chapter 3 -- reference solution (Proof)."""
# level: proof
import math


def numerical_pdf(cdf, x, h=1e-5):
    return (cdf(x + h) - cdf(x - h)) / (2 * h)


def change_of_variables(fx, hprime):
    return fx * abs(hprime)


def square_uniform_pdf(y):
    return 1.0 / (2.0 * math.sqrt(y))


def main():
    cdf = lambda x: 1 - math.exp(-x)
    print("numerical pdf at 1 :", numerical_pdf(cdf, 1.0))
    print("change_of_vars     :", change_of_variables(2.0, -3.0))
    print("square_uniform(.25):", square_uniform_pdf(0.25))


if __name__ == "__main__":
    main()
