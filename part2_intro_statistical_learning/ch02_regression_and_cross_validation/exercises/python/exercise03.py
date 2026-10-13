"""
Chapter 2 exercise -- Bias-variance decomposition (Proof tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch02_text.tex Section 2. `preds` are the
predictions at one test point from many fitted models; `truth` is f(x0).

Run with:  python3 exercise03.py
Reference solution: solutions/exercise03_solution.py
"""
# level: proof
def squared_bias(preds, truth):
    """(mean(preds) - truth)^2."""
    raise NotImplementedError("TODO: squared_bias")


def estimator_variance(preds):
    """Population variance of preds: mean((p - mean(preds))^2)."""
    raise NotImplementedError("TODO: estimator_variance")


def expected_mse(preds, truth):
    """mean((p - truth)^2) -- which equals squared_bias + variance."""
    raise NotImplementedError("TODO: expected_mse")


def main():
    preds, truth = [2.0, 4.0, 6.0], 5.0
    print("bias^2   :", squared_bias(preds, truth))
    print("variance :", estimator_variance(preds))
    print("MSE      :", expected_mse(preds, truth))


if __name__ == "__main__":
    main()
