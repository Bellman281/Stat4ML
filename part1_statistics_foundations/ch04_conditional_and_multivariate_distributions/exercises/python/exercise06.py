"""
Chapter 4 exercise -- Conditioning the normal (Research tier)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch04_text.tex Section 3 (the bivariate
and multivariate normal conditional formulas).

Run with:  python3 exercise06.py
Reference solution: solutions/exercise06_solution.py
"""
# level: research
def bvn_conditional_mean(mu_y, rho, sy, sx, x, mu_x):
    """E[Y|X=x] = mu_y + rho * (sy/sx) * (x - mu_x)."""
    raise NotImplementedError("TODO: bvn_conditional_mean")


def bvn_conditional_var(sy, rho):
    """Var(Y|X) = sy^2 * (1 - rho^2)."""
    raise NotImplementedError("TODO: bvn_conditional_var")


def mvn_conditional_mean_1d(mu1, s12, s22, x2, mu2):
    """Scalar case of mu_1 + Sigma_12 Sigma_22^{-1} (x2 - mu2)."""
    raise NotImplementedError("TODO: mvn_conditional_mean_1d")


def main():
    print("E[Y|X=2]      :", bvn_conditional_mean(0.0, 0.7, 2.0, 1.0, 2.0, 0.0))
    print("Var(Y|X)      :", bvn_conditional_var(2.0, 0.7))
    print("MVN cond mean :", mvn_conditional_mean_1d(0.0, 0.7, 1.0, 2.0, 0.0))


if __name__ == "__main__":
    main()
