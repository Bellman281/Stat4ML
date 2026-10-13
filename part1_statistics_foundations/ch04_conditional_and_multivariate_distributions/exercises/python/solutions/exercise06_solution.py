"""Chapter 4 -- reference solution (Research)."""
# level: research
def bvn_conditional_mean(mu_y, rho, sy, sx, x, mu_x):
    return mu_y + rho * (sy / sx) * (x - mu_x)


def bvn_conditional_var(sy, rho):
    return sy ** 2 * (1 - rho ** 2)


def mvn_conditional_mean_1d(mu1, s12, s22, x2, mu2):
    return mu1 + (s12 / s22) * (x2 - mu2)


def main():
    print("E[Y|X=2]      :", bvn_conditional_mean(0.0, 0.7, 2.0, 1.0, 2.0, 0.0))
    print("Var(Y|X)      :", bvn_conditional_var(2.0, 0.7))
    print("MVN cond mean :", mvn_conditional_mean_1d(0.0, 0.7, 1.0, 2.0, 0.0))


if __name__ == "__main__":
    main()
