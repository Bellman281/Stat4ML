"""
Chapter 3 exercise -- the Robbins-Monro conditions (Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch03_text.tex Section 2. Convergence needs
sum a_t = infinity and sum a_t^2 < infinity. For a_t = 1/t^p, the harmonic-type
sum diverges iff p <= 1, and the squared sum converges iff 2p > 1 (p > 1/2), so
the schedule is VALID iff 1/2 < p <= 1.
  - harmonic_partial : sum_{t=1}^T 1/t.
  - basel_partial    : sum_{t=1}^T 1/t^2  (approaches pi^2/6).
  - rm_valid         : True iff the exponent p gives a valid schedule.

Run with:  python3 exercise04.py
Reference solution: solutions/exercise04_solution.py
"""
# level: proof


def harmonic_partial(T):
    """Partial sum of 1/t for t = 1..T."""
    raise NotImplementedError("TODO: harmonic_partial")


def basel_partial(T):
    """Partial sum of 1/t^2 for t = 1..T."""
    raise NotImplementedError("TODO: basel_partial")


def rm_valid(p):
    """True iff a_t = 1/t^p satisfies both Robbins-Monro conditions
    (1/2 < p <= 1)."""
    raise NotImplementedError("TODO: rm_valid")


def main():
    print("harmonic_partial(4):", harmonic_partial(4))
    print("basel_partial(1000) :", basel_partial(1000), "  (pi^2/6 = 1.6449..)")
    for p in (1.0, 0.75, 0.5, 0.4):
        print(f"rm_valid({p}) :", rm_valid(p))


if __name__ == "__main__":
    main()
