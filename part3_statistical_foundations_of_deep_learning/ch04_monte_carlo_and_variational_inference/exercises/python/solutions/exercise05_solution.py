"""Chapter 4 -- reference solution (Proof)."""
# level: proof


def importance_weight(px, qx):
    return px / qx


def is_estimate(fvals, pxs, qxs):
    n = len(fvals)
    return sum(f * (p / q) for f, p, q in zip(fvals, pxs, qxs)) / n


def eff_sample_size(weights):
    s1 = sum(weights)
    s2 = sum(w ** 2 for w in weights)
    return s1 ** 2 / s2


def main():
    print("importance_weight :", importance_weight(0.1, 0.2))
    print("is_estimate       :", is_estimate([1.0, 1.0], [0.2, 0.2], [0.4, 0.4]))
    print("eff_sample_size u :", eff_sample_size([1, 1, 1, 1]))
    print("eff_sample_size s :", eff_sample_size([2, 0, 0, 0]))


if __name__ == "__main__":
    main()
