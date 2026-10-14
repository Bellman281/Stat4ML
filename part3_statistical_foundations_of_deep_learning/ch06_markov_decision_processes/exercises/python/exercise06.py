"""
Chapter 6 exercise -- MDP value backups (Core tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch06_text.tex Sections 1-2.
  - discounted_return : sum_t gamma^t * r_t over a reward sequence.
  - q_backup          : r + gamma * sum_s' P(s') V(s'), one action's Bellman backup.
  - greedy_action     : the index of the largest Q-value.

Run with:  python3 exercise06.py
Reference solution: solutions/exercise06_solution.py
"""
# level: core


def discounted_return(rewards, gamma):
    """sum_{t>=0} gamma^t * rewards[t]."""
    raise NotImplementedError("TODO: discounted_return")


def q_backup(r, gamma, next_values, probs):
    """One-action Bellman backup: r + gamma * sum_i probs[i] * next_values[i]."""
    raise NotImplementedError("TODO: q_backup")


def greedy_action(q_values):
    """Index of the maximum Q-value."""
    raise NotImplementedError("TODO: greedy_action")


def main():
    print("discounted_return :", discounted_return([1, 1, 1], 0.5))
    print("q_backup          :", q_backup(0.0, 0.9, [10.0, 0.0], [0.8, 0.2]))
    print("greedy_action     :", greedy_action([1.0, 5.0, 3.0]))


if __name__ == "__main__":
    main()
