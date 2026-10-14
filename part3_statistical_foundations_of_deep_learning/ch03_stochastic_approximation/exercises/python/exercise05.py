"""
Chapter 3 exercise -- noise ball, stability, averaging (Research tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch03_text.tex Sections 2-3.
  - ou_stationary_var : constant-step SGD on a quadratic leaves a noise ball of
                        variance a*sigma^2 / (2H) (linear in the step a).
  - critical_lr       : gradient descent on a quadratic with curvature H is
                        stable only for a < 2/H; return the threshold 2/H.
  - polyak_var        : averaging k iterates divides the stationary variance by k.

Run with:  python3 exercise05.py
Reference solution: solutions/exercise05_solution.py
"""
# level: research


def ou_stationary_var(lr, sigma2, H):
    """Stationary variance of constant-step SGD: lr * sigma2 / (2 * H)."""
    raise NotImplementedError("TODO: ou_stationary_var")


def critical_lr(H):
    """Largest stable constant step for curvature H: 2 / H."""
    raise NotImplementedError("TODO: critical_lr")


def polyak_var(stationary_var, k):
    """Variance after averaging k iterates: stationary_var / k."""
    raise NotImplementedError("TODO: polyak_var")


def main():
    v = ou_stationary_var(0.1, 1.0, 2.0)
    print("ou_stationary_var:", v)
    print("critical_lr      :", critical_lr(2.0))
    print("polyak_var (k=10):", polyak_var(v, 10))


if __name__ == "__main__":
    main()
