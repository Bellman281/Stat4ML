"""Chapter 4 -- reference solution (Core)."""
# level: core
import math


def predict(p, q):
    return sum(pi * qi for pi, qi in zip(p, q))


def squared_error(r, p, q):
    e = r - predict(p, q)
    return e * e


def rmse(preds, actuals):
    n = len(preds)
    mse = sum((pr - ac) ** 2 for pr, ac in zip(preds, actuals)) / n
    return math.sqrt(mse)


def main():
    print("predict        :", predict([1.0, 2.0], [2.0, 0.5]))
    print("squared_error  :", squared_error(5.0, [1.0, 2.0], [2.0, 0.5]))
    print("rmse           :", rmse([3.0, 2.0, 5.0], [4.0, 2.0, 4.0]))


if __name__ == "__main__":
    main()
