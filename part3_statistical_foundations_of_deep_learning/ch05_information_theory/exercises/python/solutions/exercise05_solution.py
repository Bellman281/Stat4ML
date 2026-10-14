"""Chapter 5 -- reference solution (Core)."""
# level: core
import math


def entropy(p):
    return -sum(pi * math.log(pi) for pi in p)


def cross_entropy(p, q):
    return -sum(pi * math.log(qi) for pi, qi in zip(p, q))


def kl(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q))


def main():
    p = [0.5, 0.5]; q = [0.25, 0.75]
    print("entropy      :", entropy(p))
    print("cross_entropy:", cross_entropy(p, q))
    print("kl           :", kl(p, q))


if __name__ == "__main__":
    main()
