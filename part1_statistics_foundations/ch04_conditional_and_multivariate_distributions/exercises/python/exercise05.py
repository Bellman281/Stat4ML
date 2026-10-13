"""
Chapter 4 exercise -- Total expectation and total variance (Proof tier)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch04_text.tex Section 2. The inputs
describe groups Y=1..k with within-group means, within-group variances, and
weights P(Y=y).

Run with:  python3 exercise05.py
Reference solution: solutions/exercise05_solution.py
"""
# level: proof
def group_mean(means, weights):
    """E[X] = E[E[X|Y]] = sum_y weight_y * mean_y."""
    raise NotImplementedError("TODO: group_mean")


def within_var(vars_, weights):
    """E[Var(X|Y)] = sum_y weight_y * var_y."""
    raise NotImplementedError("TODO: within_var")


def between_var(means, weights):
    """Var(E[X|Y]) = sum_y weight_y * mean_y^2 - (sum_y weight_y * mean_y)^2."""
    raise NotImplementedError("TODO: between_var")


def total_variance(vars_, means, weights):
    """Var(X) = within_var + between_var."""
    raise NotImplementedError("TODO: total_variance")


def main():
    w, m, v = [0.5, 0.5], [0.0, 10.0], [1.0, 1.0]
    print("E[X]        :", group_mean(m, w))
    print("within var  :", within_var(v, w))
    print("between var :", between_var(m, w))
    print("total var   :", total_variance(v, m, w))


if __name__ == "__main__":
    main()
