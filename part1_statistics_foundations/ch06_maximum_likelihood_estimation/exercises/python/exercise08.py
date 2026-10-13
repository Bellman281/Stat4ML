"""
Chapter 6 exercise -- M-estimation & the sandwich variance (Research tier)
Part I: Statistics Foundation for ML

Working model: X ~ N(theta, 1), so the MLE of theta is the sample mean.
Implement each TODO using ch06_text.tex Section 3 (MLE as an M-estimator,
Fisher scoring, and the sandwich variance A^{-1} B A^{-1}).

Run with:  python3 exercise08.py
Reference solution: solutions/exercise08_solution.py
"""
# level: research
import math


def avg_negloglik(theta, data):
    """Average per-observation NLL of N(theta,1):
    mean over data of 0.5*(x-theta)^2 + 0.5*log(2*pi)."""
    raise NotImplementedError("TODO: avg_negloglik")


def fisher_scoring_mean(data, init, iters):
    """Fisher scoring under N(theta,1): repeat
    theta <- theta + (1/n) * sum_i (x_i - theta)."""
    raise NotImplementedError("TODO: fisher_scoring_mean")


def naive_variance(data):
    """Inverse-Fisher variance of theta_hat under N(theta,1): 1/n."""
    raise NotImplementedError("TODO: naive_variance")


def sandwich_variance(data, theta):
    """Robust variance A^{-1} B A^{-1} with A = n and
    B = sum_i (x_i - theta)^2, i.e. sum_i (x_i-theta)^2 / n^2."""
    raise NotImplementedError("TODO: sandwich_variance")


def main():
    data = [1.0, 3.0, 2.0, 6.0, 4.0, 2.0, 5.0, 1.0]  # mean 3.0, spread > 1
    th = fisher_scoring_mean(data, init=0.0, iters=1)
    print(f"Fisher scoring theta = {th}  (expect 3.0)")
    print(f"avg NLL at 3.0       = {avg_negloglik(3.0, data):.4f}")
    print(f"naive var (1/n)      = {naive_variance(data)}")
    print(f"sandwich var         = {sandwich_variance(data, th)}  (>> naive if misspecified)")


if __name__ == "__main__":
    main()
