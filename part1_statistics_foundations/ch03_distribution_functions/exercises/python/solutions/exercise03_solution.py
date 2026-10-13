"""Chapter 3 -- reference solution (Core)."""
# level: core
import math


def exponential_cdf(x, rate):
    return 1 - math.exp(-rate * x)


def exponential_pdf(x, rate):
    return rate * math.exp(-rate * x)


def inverse_transform_exponential(u, rate):
    return -math.log(1 - u) / rate


def empirical_cdf(data, x):
    return sum(1 for d in data if d <= x) / len(data)


def main():
    print("F(ln2, rate=1) :", exponential_cdf(math.log(2), 1.0))
    print("f(0, rate=1)   :", exponential_pdf(0.0, 1.0))
    print("Finv(0.5)      :", inverse_transform_exponential(0.5, 1.0))
    print("ecdf at 2.5    :", empirical_cdf([1, 2, 3, 4], 2.5))


if __name__ == "__main__":
    main()
