"""
Chapter 1 exercise -- Hoeffding and the finite-class bound (Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch01_text.tex Section 2.
  - hoeffding_tail  : the tail probability 2 exp(-2 n eps^2) (loss in [0,1]).
  - confidence_width: invert it -- the eps for which the tail equals delta,
                      eps = sqrt( log(2/delta) / (2n) ).
  - finite_class_bound: Rhat + sqrt( (log|H| + log(2/delta)) / (2n) ).

Run with:  python3 exercise02.py
Reference solution: solutions/exercise02_solution.py
"""
# level: proof
import math


def hoeffding_tail(n, eps):
    """Two-sided Hoeffding tail probability for a [0,1]-bounded mean."""
    raise NotImplementedError("TODO: hoeffding_tail")


def confidence_width(n, delta):
    """Half-width eps such that hoeffding_tail(n, eps) = delta."""
    raise NotImplementedError("TODO: confidence_width")


def finite_class_bound(emp_risk, m, n, delta):
    """Finite-class generalisation bound for |H| = m hypotheses."""
    raise NotImplementedError("TODO: finite_class_bound")


def main():
    print("hoeffding_tail(100,0.1):", hoeffding_tail(100, 0.1))
    print("confidence_width(200)  :", confidence_width(200, 0.05))
    print("finite_class_bound     :", finite_class_bound(0.1, 1000, 500, 0.05))


if __name__ == "__main__":
    main()
