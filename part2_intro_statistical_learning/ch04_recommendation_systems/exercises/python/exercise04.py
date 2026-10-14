"""
Chapter 4 exercise -- the latent-factor prediction (Core tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch04_text.tex Section 1. A rating is the
dot product of a user factor and an item factor; the squared error scores one
prediction; RMSE scores a whole set. (RMSE = *root* mean squared error.)

Run with:  python3 exercise04.py
Reference solution: solutions/exercise04_solution.py
"""
# level: core
import math


def predict(p, q):
    """Predicted rating = p . q  (dot product of the two latent vectors)."""
    raise NotImplementedError("TODO: predict")


def squared_error(r, p, q):
    """(r - p.q)^2 for one observed rating r."""
    raise NotImplementedError("TODO: squared_error")


def rmse(preds, actuals):
    """sqrt( mean( (pred - actual)^2 ) ) over the two aligned lists."""
    raise NotImplementedError("TODO: rmse")


def main():
    print("predict        :", predict([1.0, 2.0], [2.0, 0.5]))
    print("squared_error  :", squared_error(5.0, [1.0, 2.0], [2.0, 0.5]))
    print("rmse           :", rmse([3.0, 2.0, 5.0], [4.0, 2.0, 4.0]))


if __name__ == "__main__":
    main()
