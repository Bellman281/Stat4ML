"""Chapter 2 -- reference solution (Core)."""
# level: core
def ols_slope(x, y):
    xbar = sum(x) / len(x); ybar = sum(y) / len(y)
    sxy = sum((xi - xbar) * (yi - ybar) for xi, yi in zip(x, y))
    sxx = sum((xi - xbar) ** 2 for xi in x)
    return sxy / sxx


def ols_intercept(x, y):
    xbar = sum(x) / len(x); ybar = sum(y) / len(y)
    return ybar - ols_slope(x, y) * xbar


def predict(b0, b1, x):
    return b0 + b1 * x


def r_squared(x, y, b0, b1):
    ybar = sum(y) / len(y)
    ss_res = sum((yi - (b0 + b1 * xi)) ** 2 for xi, yi in zip(x, y))
    ss_tot = sum((yi - ybar) ** 2 for yi in y)
    return 1 - ss_res / ss_tot


def main():
    x = [0, 1, 2, 3]; y = [1, 3, 5, 7]
    b1 = ols_slope(x, y); b0 = ols_intercept(x, y)
    print("slope, intercept :", b1, b0)
    print("predict at 10    :", predict(b0, b1, 10))
    print("R^2              :", r_squared(x, y, b0, b1))


if __name__ == "__main__":
    main()
