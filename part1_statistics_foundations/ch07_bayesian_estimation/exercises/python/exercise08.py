"""
Chapter 7 exercise -- Normal-Normal conjugacy (Proof tier)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch07_text.tex Section 2 (precisions add,
and the posterior mean is a precision-weighted average). Prior N(mu0, tau2);
n observations of mean xbar from N(theta, sigma2).

Run with:  python3 exercise08.py
Reference solution: solutions/exercise08_solution.py
"""
# level: proof
def normal_posterior_precision(tau2, sigma2, n):
    """Posterior precision: 1/tau2 + n/sigma2."""
    raise NotImplementedError("TODO: normal_posterior_precision")


def normal_posterior_mean(mu0, tau2, xbar, sigma2, n):
    """Posterior mean: (mu0/tau2 + n*xbar/sigma2) / precision."""
    raise NotImplementedError("TODO: normal_posterior_mean")


def normal_posterior_var(tau2, sigma2, n):
    """Posterior variance: 1 / precision."""
    raise NotImplementedError("TODO: normal_posterior_var")


def main():
    print("precision :", normal_posterior_precision(1.0, 1.0, 10))
    print("mean      :", normal_posterior_mean(0.0, 1.0, 2.0, 1.0, 10))
    print("variance  :", normal_posterior_var(1.0, 1.0, 10))


if __name__ == "__main__":
    main()
