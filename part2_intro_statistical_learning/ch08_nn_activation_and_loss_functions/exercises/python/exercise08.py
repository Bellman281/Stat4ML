"""
Chapter 8 exercise -- activation functions (Core tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch08_text.tex Section 1. Three activations:
two scalar (sigmoid, relu) and one vector (softmax). softmax must be the
NUMERICALLY STABLE version -- subtract the max logit before exponentiating.

Run with:  python3 exercise08.py
Reference solution: solutions/exercise08_solution.py
"""
# level: core
import math


def sigmoid(z):
    """1 / (1 + e^{-z})."""
    raise NotImplementedError("TODO: sigmoid")


def relu(z):
    """max(0, z)."""
    raise NotImplementedError("TODO: relu")


def softmax(zs):
    """Stable softmax of a list of logits -> list of probabilities that sum to 1.
    Subtract max(zs) from every logit before exponentiating."""
    raise NotImplementedError("TODO: softmax")


def main():
    print("sigmoid(0) :", sigmoid(0))
    print("relu(-2,3) :", relu(-2), relu(3))
    print("softmax    :", softmax([1.0, 1.0, 1.0]))
    print("softmax big:", softmax([1000.0, 1000.0]))  # must not overflow


if __name__ == "__main__":
    main()
