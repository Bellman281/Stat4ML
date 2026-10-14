"""Chapter 1 -- reference solution (Research)."""
# level: research
import math


def sauer_bound(n, d):
    return sum(math.comb(n, i) for i in range(0, d + 1))


def vc_bound_term(d, n, delta):
    return math.sqrt((d * (math.log(2 * n / d) + 1) + math.log(4 / delta)) / n)


def shatters(patterns, n):
    return len(set(patterns)) == 2 ** n


def main():
    print("sauer_bound(5,2) :", sauer_bound(5, 2))
    print("vc_bound_term    :", vc_bound_term(10, 1000, 0.05))
    full = [(0, 0), (0, 1), (1, 0), (1, 1)]
    print("shatters(full,2) :", shatters(full, 2))
    print("shatters(part,2) :", shatters([(0, 0), (1, 1)], 2))


if __name__ == "__main__":
    main()
