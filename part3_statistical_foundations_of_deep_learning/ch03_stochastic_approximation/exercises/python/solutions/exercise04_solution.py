"""Chapter 3 -- reference solution (Proof)."""
# level: proof


def harmonic_partial(T):
    return sum(1.0 / t for t in range(1, T + 1))


def basel_partial(T):
    return sum(1.0 / t ** 2 for t in range(1, T + 1))


def rm_valid(p):
    return (p > 0.5) and (p <= 1.0)


def main():
    print("harmonic_partial(4):", harmonic_partial(4))
    print("basel_partial(1000) :", basel_partial(1000), "  (pi^2/6 = 1.6449..)")
    for p in (1.0, 0.75, 0.5, 0.4):
        print(f"rm_valid({p}) :", rm_valid(p))


if __name__ == "__main__":
    main()
