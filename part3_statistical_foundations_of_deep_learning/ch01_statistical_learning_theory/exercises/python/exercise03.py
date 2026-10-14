"""
Chapter 1 exercise -- VC capacity (Research tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch01_text.tex Section 3.
  - sauer_bound : Sauer-Shelah -- a class of VC dimension d realises at most
                  sum_{i=0}^d C(n, i) dichotomies on n points.
  - vc_bound_term: the capacity term sqrt( (d(log(2n/d)+1) + log(4/delta)) / n ).
  - shatters    : does the observed set of label patterns cover all 2^n
                  labelings of n points? (then the class shatters them.)

Run with:  python3 exercise03.py
Reference solution: solutions/exercise03_solution.py
"""
# level: research
import math


def sauer_bound(n, d):
    """Max number of dichotomies: sum_{i=0}^d C(n, i)."""
    raise NotImplementedError("TODO: sauer_bound")


def vc_bound_term(d, n, delta):
    """VC generalisation term sqrt((d*(log(2n/d)+1) + log(4/delta)) / n)."""
    raise NotImplementedError("TODO: vc_bound_term")


def shatters(patterns, n):
    """True iff `patterns` (an iterable of 0/1 tuples of length n) contains all
    2^n possible labelings."""
    raise NotImplementedError("TODO: shatters")


def main():
    print("sauer_bound(5,2) :", sauer_bound(5, 2))
    print("vc_bound_term    :", vc_bound_term(10, 1000, 0.05))
    full = [(0, 0), (0, 1), (1, 0), (1, 1)]
    print("shatters(full,2) :", shatters(full, 2))
    print("shatters(part,2) :", shatters([(0, 0), (1, 1)], 2))


if __name__ == "__main__":
    main()
