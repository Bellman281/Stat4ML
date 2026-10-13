"""
Chapter 3 exercise -- Penalties and the elastic net (Research tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch03_text.tex Section 3 (the L1 and L2
penalties and their elastic-net combination).

Run with:  python3 exercise05.py
Reference solution: solutions/exercise05_solution.py
"""
# level: research
def l1_penalty(beta, lam):
    """lam * sum(|b|)."""
    raise NotImplementedError("TODO: l1_penalty")


def l2_penalty(beta, lam):
    """lam * sum(b^2)."""
    raise NotImplementedError("TODO: l2_penalty")


def elastic_net_penalty(beta, lam, alpha):
    """lam * ( alpha * sum(|b|) + (1 - alpha) * sum(b^2) )."""
    raise NotImplementedError("TODO: elastic_net_penalty")


def main():
    b = [1.0, -2.0, 3.0]
    print("l1          :", l1_penalty(b, 1.0))
    print("l2          :", l2_penalty(b, 1.0))
    print("elastic net :", elastic_net_penalty(b, 1.0, 0.25))


if __name__ == "__main__":
    main()
