"""
Chapter 1 exercise -- risk and the generalisation gap (Core tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch01_text.tex Section 1. The empirical risk
is the average loss on the sample; the generalisation gap is how much worse the
true risk is than the empirical one.

Run with:  python3 exercise01.py
Reference solution: solutions/exercise01_solution.py
"""
# level: core


def zero_one_loss(pred, y):
    """0-1 loss: 0.0 if the prediction is correct, 1.0 if it is wrong."""
    raise NotImplementedError("TODO: zero_one_loss")


def empirical_risk(preds, ys):
    """Mean 0-1 loss over the sample: (1/n) sum_i zero_one_loss(preds_i, ys_i)."""
    raise NotImplementedError("TODO: empirical_risk")


def generalisation_gap(emp_risk, true_risk):
    """The gap R(h) - Rhat(h): true risk minus empirical risk."""
    raise NotImplementedError("TODO: generalisation_gap")


def main():
    preds = [1, 0, 1, 1]; ys = [1, 1, 1, 0]
    print("zero_one(1,1) :", zero_one_loss(1, 1))
    print("zero_one(1,0) :", zero_one_loss(1, 0))
    print("empirical_risk:", empirical_risk(preds, ys))
    print("gap(0.3,0.5)  :", generalisation_gap(0.3, 0.5))


if __name__ == "__main__":
    main()
