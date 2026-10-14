"""Chapter 2 -- reference solution (Proof)."""
# level: proof


def gaussian_log_prior(w, tau):
    return -w ** 2 / (2 * tau ** 2)


def ridge_lambda(sigma2, tau2):
    return sigma2 / tau2


def ridge_estimate_1d(xs, ys, lam):
    sxy = sum(x * y for x, y in zip(xs, ys))
    sxx = sum(x * x for x in xs)
    return sxy / (sxx + lam)


def main():
    xs = [1, 2, 3]; ys = [2, 4, 6]
    print("gaussian_log_prior:", gaussian_log_prior(2.0, 1.0))
    print("ridge_lambda      :", ridge_lambda(1.0, 0.5))
    print("ridge (lam=0, OLS):", ridge_estimate_1d(xs, ys, 0.0))
    print("ridge (lam=14)    :", ridge_estimate_1d(xs, ys, 14.0))


if __name__ == "__main__":
    main()
