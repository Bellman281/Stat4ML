"""
Chapter 6 exercise -- Hard EM and monotonicity (Research tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch06_text.tex Section 3 (the hard,
winner-takes-all assignment that links EM to k-means, the mixing-weight
update, and the monotone likelihood gap).

Run with:  python3 exercise08.py
Reference solution: solutions/exercise08_solution.py
"""
# level: research
def hard_assignment(resp):
    """Index of the component with the largest responsibility (argmax)."""
    raise NotImplementedError("TODO: hard_assignment")


def responsibility_based_weight(resp_column):
    """New mixing weight pi_k = mean of a component's responsibilities."""
    raise NotImplementedError("TODO: responsibility_based_weight")


def em_lower_bound_gap(ll_before, ll_after):
    """ll_after - ll_before, which EM guarantees is >= 0."""
    raise NotImplementedError("TODO: em_lower_bound_gap")


def main():
    print("hard_assignment :", hard_assignment([0.2, 0.7, 0.1]))
    print("weight          :", responsibility_based_weight([0.5, 0.5, 1.0, 0.0]))
    print("em gap          :", em_lower_bound_gap(1.0, 1.5))


if __name__ == "__main__":
    main()
