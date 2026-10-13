"""
Chapter 2 exercise -- Linear regression (Core)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch02_text.tex Section 1 (the
simple-linear-regression formulas and R^2).

Run with:  python3 exercise02.py
Reference solution: solutions/exercise02_solution.py
"""
# level: core
def ols_slope(x, y):
    """Slope = sum((xi-xbar)(yi-ybar)) / sum((xi-xbar)^2)."""
    raise NotImplementedError("TODO: ols_slope")


def ols_intercept(x, y):
    """Intercept = ybar - slope * xbar."""
    raise NotImplementedError("TODO: ols_intercept")


def predict(b0, b1, x):
    """Fitted value b0 + b1 * x for a single x."""
    raise NotImplementedError("TODO: predict")


def r_squared(x, y, b0, b1):
    """R^2 = 1 - SS_res / SS_tot."""
    raise NotImplementedError("TODO: r_squared")


def main():
    x = [0, 1, 2, 3]; y = [1, 3, 5, 7]          # exactly y = 2x + 1
    b1 = ols_slope(x, y); b0 = ols_intercept(x, y)
    print("slope, intercept :", b1, b0)
    print("predict at 10    :", predict(b0, b1, 10))
    print("R^2              :", r_squared(x, y, b0, b1))


if __name__ == "__main__":
    main()
