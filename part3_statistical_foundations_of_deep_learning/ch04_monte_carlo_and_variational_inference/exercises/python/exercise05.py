"""
Chapter 4 exercise -- importance sampling (Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch04_text.tex Section 1.
  - importance_weight : the density ratio w = p(x)/q(x).
  - is_estimate       : (1/n) sum_i f_i * p_i/q_i, the importance-sampling estimate.
  - eff_sample_size   : the ESS diagnostic (sum w)^2 / sum(w^2).

The test checks that importance sampling with q = p reduces to plain Monte Carlo.

Run with:  python3 exercise05.py
Reference solution: solutions/exercise05_solution.py
"""
# level: proof


def importance_weight(px, qx):
    """Density ratio p(x) / q(x)."""
    raise NotImplementedError("TODO: importance_weight")


def is_estimate(fvals, pxs, qxs):
    """Importance-sampling estimate: mean of f_i * p_i/q_i."""
    raise NotImplementedError("TODO: is_estimate")


def eff_sample_size(weights):
    """Effective sample size: (sum w)^2 / sum(w^2)."""
    raise NotImplementedError("TODO: eff_sample_size")


def main():
    print("importance_weight :", importance_weight(0.1, 0.2))
    print("is_estimate       :", is_estimate([1.0, 1.0], [0.2, 0.2], [0.4, 0.4]))
    print("eff_sample_size u :", eff_sample_size([1, 1, 1, 1]))
    print("eff_sample_size s :", eff_sample_size([2, 0, 0, 0]))


if __name__ == "__main__":
    main()
