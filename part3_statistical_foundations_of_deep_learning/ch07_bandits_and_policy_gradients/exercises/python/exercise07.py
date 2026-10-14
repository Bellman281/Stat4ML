"""
Chapter 7 exercise -- bandit action selection (Core tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch07_text.tex Section 1.
  - ucb_index         : mean + sqrt(c * log(t) / n), the optimistic arm value.
  - argmax_index      : index of the largest value (greedy / UCB pick).
  - cumulative_regret : sum_t (mu_star - mu_chosen[t]).

Run with:  python3 exercise07.py
Reference solution: solutions/exercise07_solution.py
"""
# level: core
import math


def ucb_index(mean, n, t, c):
    """UCB index: mean + sqrt(c * log(t) / n)."""
    raise NotImplementedError("TODO: ucb_index")


def argmax_index(values):
    """Index of the maximum value."""
    raise NotImplementedError("TODO: argmax_index")


def cumulative_regret(mu_star, chosen_means):
    """Total regret: sum over rounds of (mu_star - chosen mean)."""
    raise NotImplementedError("TODO: cumulative_regret")


def main():
    print("ucb_index         :", ucb_index(0.5, 4, 100, 2.0))
    print("argmax_index      :", argmax_index([1.0, 5.0, 3.0]))
    print("cumulative_regret :", cumulative_regret(1.0, [0.8, 0.9, 1.0]))


if __name__ == "__main__":
    main()
