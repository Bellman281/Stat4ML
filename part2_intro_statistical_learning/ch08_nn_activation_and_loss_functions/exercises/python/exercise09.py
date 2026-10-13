"""
Chapter 8 exercise -- softmax cross-entropy and its gradient (Proof tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch08_text.tex Section 2. You build the
classification head and then the result the whole chapter turns on: the
gradient of the loss at the logits is exactly p - y. The test confirms it
against a finite-difference gradient, so a wrong formula is caught.

y is a one-hot list. Run with:  python3 exercise09.py
Reference solution: solutions/exercise09_solution.py
"""
# level: proof
import math


def softmax(zs):
    m = max(zs)
    exps = [math.exp(z - m) for z in zs]
    tot = sum(exps)
    return [e / tot for e in exps]


def cross_entropy(p, y):
    """L = - sum_k y_k * log(p_k)."""
    raise NotImplementedError("TODO: cross_entropy")


def ce_grad(p, y):
    """Gradient of cross-entropy wrt the LOGITS: dL/dz_k = p_k - y_k."""
    raise NotImplementedError("TODO: ce_grad")


def main():
    z = [2.0, 0.5, -1.0]
    y = [1.0, 0.0, 0.0]
    p = softmax(z)
    print("p         :", p)
    print("loss      :", cross_entropy(p, y))
    print("grad (p-y):", ce_grad(p, y))


if __name__ == "__main__":
    main()
