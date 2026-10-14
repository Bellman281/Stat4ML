"""
Chapter 6 exercise -- Monte Carlo and TD updates (Research tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch06_text.tex Section 3.
  - mc_update : V(s) <- V(s) + alpha (G - V(s)), moving toward the return.
  - td_error  : r + gamma V(s') - V(s), the one-step temporal-difference error.
  - td_update : V(s) <- V(s) + alpha * td_error(...), the bootstrapped update.

Run with:  python3 exercise08.py
Reference solution: solutions/exercise08_solution.py
"""
# level: research


def mc_update(v, G, alpha):
    """Monte Carlo update toward the observed return G."""
    raise NotImplementedError("TODO: mc_update")


def td_error(r, gamma, v_next, v):
    """One-step TD error: r + gamma * v_next - v."""
    raise NotImplementedError("TODO: td_error")


def td_update(v, r, gamma, v_next, alpha):
    """TD(0) update: v + alpha * td_error(r, gamma, v_next, v)."""
    raise NotImplementedError("TODO: td_update")


def main():
    print("mc_update :", mc_update(0.5, 1.0, 0.1))
    print("td_error  :", td_error(0.0, 0.9, 1.0, 0.5))
    print("td_update :", td_update(0.5, 0.0, 0.9, 1.0, 0.1))


if __name__ == "__main__":
    main()
