"""
Chapter 4 exercise -- Joint, marginal, conditional (Core)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch04_text.tex Section 1. `joint` is a
dict {(x, y): P(X=x, Y=y)}.

Run with:  python3 exercise04.py
Reference solution: solutions/exercise04_solution.py
"""
# level: core
JOINT = {(0, 0): 0.3, (0, 1): 0.2, (1, 0): 0.1, (1, 1): 0.4}


def marginal_x_prob(joint, x0):
    """P(X = x0): sum the joint over all y."""
    raise NotImplementedError("TODO: marginal_x_prob")


def conditional_y_prob(joint, y0, x0):
    """P(Y = y0 | X = x0) = P(X=x0, Y=y0) / P(X=x0)."""
    raise NotImplementedError("TODO: conditional_y_prob")


def joint_covariance(joint):
    """Cov(X, Y) = E[XY] - E[X] E[Y]."""
    raise NotImplementedError("TODO: joint_covariance")


def main():
    print("P(X=0)        :", marginal_x_prob(JOINT, 0))
    print("P(Y=1 | X=0)  :", conditional_y_prob(JOINT, 1, 0))
    print("P(Y=1 | X=1)  :", conditional_y_prob(JOINT, 1, 1))
    print("Cov(X,Y)      :", joint_covariance(JOINT))


if __name__ == "__main__":
    main()
