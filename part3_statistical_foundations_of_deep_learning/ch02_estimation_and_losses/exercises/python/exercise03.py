"""
Chapter 2 exercise -- MAP = penalised MLE (Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch02_text.tex Section 2.
  - gaussian_log_prior : the w-dependent part of log N(0, tau^2): -w^2/(2 tau^2).
  - ridge_lambda       : the penalty strength a Gaussian prior induces, sigma^2/tau^2.
  - ridge_estimate_1d  : the 1-D ridge / MAP point estimate, sum(x y)/(sum(x^2)+lam).

The test checks the chapter's claim: the MAP estimate with lam = sigma^2/tau^2
equals the minimiser of the penalised objective.

Run with:  python3 exercise03.py
Reference solution: solutions/exercise03_solution.py
"""
# level: proof


def gaussian_log_prior(w, tau):
    """w-dependent part of the Gaussian log-prior: -w^2 / (2 tau^2)."""
    raise NotImplementedError("TODO: gaussian_log_prior")


def ridge_lambda(sigma2, tau2):
    """Ridge penalty induced by a N(0, tau2) prior under N(.,sigma2) noise."""
    raise NotImplementedError("TODO: ridge_lambda")


def ridge_estimate_1d(xs, ys, lam):
    """1-D ridge estimate: sum(x*y) / (sum(x^2) + lam)."""
    raise NotImplementedError("TODO: ridge_estimate_1d")


def main():
    xs = [1, 2, 3]; ys = [2, 4, 6]
    print("gaussian_log_prior:", gaussian_log_prior(2.0, 1.0))
    print("ridge_lambda      :", ridge_lambda(1.0, 0.5))
    print("ridge (lam=0, OLS):", ridge_estimate_1d(xs, ys, 0.0))
    print("ridge (lam=14)    :", ridge_estimate_1d(xs, ys, 14.0))


if __name__ == "__main__":
    main()
