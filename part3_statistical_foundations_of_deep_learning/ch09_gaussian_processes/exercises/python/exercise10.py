"""
Chapter 9 exercise -- the GP posterior at one point (Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch09_text.tex Section 2. With a single
training point, the GP predictive mean and variance are the 1x1 case of the
closed form. k_11 = k(x1,x1), k_star = k(x*,x1), k_ss = k(x*,x*).
  - gp_post_mean : k_star / (k_11 + sigma2) * y
  - gp_post_var  : k_ss - k_star^2 / (k_11 + sigma2)

The test checks that at the training point, with no noise, the variance is 0
(the posterior is certain where it has seen data).

Run with:  python3 exercise10.py
Reference solution: solutions/exercise10_solution.py
"""
# level: proof


def gp_post_mean(k_star, k_11, sigma2, y):
    """GP predictive mean: k_star / (k_11 + sigma2) * y."""
    raise NotImplementedError("TODO: gp_post_mean")


def gp_post_var(k_ss, k_star, k_11, sigma2):
    """GP predictive variance: k_ss - k_star^2 / (k_11 + sigma2)."""
    raise NotImplementedError("TODO: gp_post_var")


def main():
    print("gp_post_mean :", gp_post_mean(0.6, 1.0, 0.1, 2.0))
    print("gp_post_var  :", gp_post_var(1.0, 0.6, 1.0, 0.1))
    # at the training point, noise-free: k_ss=k_star=k_11=1, sigma2=0
    print("var at data  :", gp_post_var(1.0, 1.0, 1.0, 0.0))


if __name__ == "__main__":
    main()
