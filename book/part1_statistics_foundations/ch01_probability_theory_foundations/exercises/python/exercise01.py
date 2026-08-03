"""
Chapter 1 exercise -- Probability Theory Foundations
Part I: Statistics Foundation for ML

HOMEWORK (course-discussion style): implement each TODO below using only
the definitions from ch01_text.tex (sample space, Kolmogorov's axioms,
inclusion-exclusion, conditional probability, Bayes' theorem) and Python's
standard library `random` module for simulation.

Do not import numpy/scipy for this exercise -- the point is to build the
axioms up from plain Python so the arithmetic is fully visible.

Run this file directly to see a short demo once you've filled in the TODOs:
    python3 exercise01.py

A full reference solution is in solutions/exercise01_solution.py -- try not
to peek until you've had a real attempt.
"""
import random


def sample_space_two_coins():
    """Return the sample space of tossing two fair coins, as a list of
    4 strings: 'HH', 'HT', 'TH', 'TT'."""
    return ["HH", "HT", "TH", "TT"]


def is_valid_probability_function(p, sample_space, tol=1e-9):
    """Check whether `p` (a dict mapping each outcome in `sample_space` to
    a probability) satisfies Kolmogorov's axioms:
      1. p[outcome] >= 0 for every outcome
      2. sum(p.values()) == 1 (within `tol`)
    `sample_space` is the full list of outcomes; `p` must have exactly
    one entry per outcome.

    Return True if valid, False otherwise.
    """
    # TODO: implement this. Remember: BOTH conditions must hold, and the
    # keys of p must exactly match sample_space (no missing/extra outcomes).
    raise NotImplementedError("TODO: is_valid_probability_function")


def complement_probability(p_a):
    """Return P(A^c) given P(A), using P(A^c) = 1 - P(A)."""
    # TODO
    raise NotImplementedError("TODO: complement_probability")


def union_probability(p_a, p_b, p_a_and_b):
    """Return P(A u B) given P(A), P(B), and P(A n B), via
    inclusion-exclusion: P(A u B) = P(A) + P(B) - P(A n B)."""
    # TODO
    raise NotImplementedError("TODO: union_probability")


def conditional_probability(p_a_and_b, p_b):
    """Return P(A | B) = P(A n B) / P(B). Assume p_b > 0."""
    # TODO
    raise NotImplementedError("TODO: conditional_probability")


def bayes_theorem(p_b_given_a, p_a, p_b):
    """Return P(A | B) via Bayes' rule:
         P(A | B) = P(B | A) * P(A) / P(B)."""
    # TODO
    raise NotImplementedError("TODO: bayes_theorem")


def bayes_theorem_partition(p_b_given_ai, p_ai):
    """Full Bayes' theorem over a partition A_1, ..., A_k of the sample
    space. `p_b_given_ai` and `p_ai` are equal-length lists, with
    p_b_given_ai[i] = P(B | A_i) and p_ai[i] = P(A_i).

    Return a list `posterior` with posterior[i] = P(A_i | B), i.e.

        P(A_i | B) = P(B|A_i) P(A_i) / sum_j P(B|A_j) P(A_j)
    """
    # TODO: use the law of total probability for the denominator.
    raise NotImplementedError("TODO: bayes_theorem_partition")


def simulate_coin_law_of_large_numbers(p_heads, n_tosses, seed=0):
    """Simulate `n_tosses` independent coin tosses with P(heads) = p_heads,
    using Python's `random.random()` seeded with `seed`, and return the
    empirical proportion of heads observed.

    This is meant to illustrate that the empirical frequency converges to
    the axiomatic probability p_heads as n_tosses grows (the intuition
    behind the Law of Large Numbers, formalized in Chapter 5).
    """
    # TODO: seed the RNG, draw n_tosses uniform(0,1) values, count how many
    # are < p_heads, and return heads_count / n_tosses.
    raise NotImplementedError("TODO: simulate_coin_law_of_large_numbers")


def main():
    ss = sample_space_two_coins()
    fair = {o: 0.25 for o in ss}
    print("Two-coin sample space:", ss)
    print("Fair distribution valid?", is_valid_probability_function(fair, ss))

    p_a, p_b, p_ab = 0.5, 0.4, 0.2
    print("P(A^c) =", complement_probability(p_a))
    print("P(A u B) =", union_probability(p_a, p_b, p_ab))
    print("P(A | B) =", conditional_probability(p_ab, p_b))
    print("Bayes P(A|B) =", bayes_theorem(p_ab / p_a, p_a, p_b))

    for n in (10, 1_000, 100_000):
        freq = simulate_coin_law_of_large_numbers(0.5, n, seed=42)
        print(f"n={n:>7}: empirical P(heads) = {freq:.4f}")


if __name__ == "__main__":
    main()
