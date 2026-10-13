"""
Chapter 3 exercise -- Logistic regression (Core)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch03_text.tex Section 1 (the sigmoid,
the linear log-odds, and the cross-entropy loss).

Run with:  python3 exercise03.py
Reference solution: solutions/exercise03_solution.py
"""
# level: core
import math


def sigmoid(z):
    """1 / (1 + exp(-z))."""
    raise NotImplementedError("TODO: sigmoid")


def logistic_proba(w, x):
    """P(y=1|x) = sigmoid(w . x). x already includes a leading 1 for the bias."""
    raise NotImplementedError("TODO: logistic_proba")


def cross_entropy(y, p):
    """-( y*log(p) + (1-y)*log(1-p) )."""
    raise NotImplementedError("TODO: cross_entropy")


def classify(p, threshold=0.5):
    """1 if p >= threshold else 0."""
    raise NotImplementedError("TODO: classify")


def main():
    print("sigmoid(0)        :", sigmoid(0.0))
    print("proba([0,1,1],.)  :", logistic_proba([0, 1, 1], [1, 2, -2]))
    print("cross_entropy     :", cross_entropy(1, 0.5))
    print("classify(0.7)     :", classify(0.7))


if __name__ == "__main__":
    main()
