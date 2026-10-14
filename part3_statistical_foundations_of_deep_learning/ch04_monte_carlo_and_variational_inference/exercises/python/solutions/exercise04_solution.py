"""Chapter 4 -- reference solution (Core)."""
# level: core
import math


def mc_estimate(fvals):
    return sum(fvals) / len(fvals)


def mc_variance(fvals):
    m = mc_estimate(fvals)
    n = len(fvals)
    return sum((x - m) ** 2 for x in fvals) / n


def mc_standard_error(fvals):
    return math.sqrt(mc_variance(fvals) / len(fvals))


def main():
    f = [2, 4, 4, 4, 5, 5, 7, 9]
    print("mc_estimate       :", mc_estimate(f))
    print("mc_variance       :", mc_variance(f))
    print("mc_standard_error :", mc_standard_error(f))


if __name__ == "__main__":
    main()
