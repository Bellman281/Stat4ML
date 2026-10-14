"""Chapter 3 -- reference solution (Research)."""
# level: research


def ou_stationary_var(lr, sigma2, H):
    return lr * sigma2 / (2 * H)


def critical_lr(H):
    return 2.0 / H


def polyak_var(stationary_var, k):
    return stationary_var / k


def main():
    v = ou_stationary_var(0.1, 1.0, 2.0)
    print("ou_stationary_var:", v)
    print("critical_lr      :", critical_lr(2.0))
    print("polyak_var (k=10):", polyak_var(v, 10))


if __name__ == "__main__":
    main()
