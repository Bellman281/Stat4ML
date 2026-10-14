"""Chapter 1 -- reference solution (Core)."""
# level: core


def zero_one_loss(pred, y):
    return 1.0 if pred != y else 0.0


def empirical_risk(preds, ys):
    return sum(zero_one_loss(p, y) for p, y in zip(preds, ys)) / len(ys)


def generalisation_gap(emp_risk, true_risk):
    return true_risk - emp_risk


def main():
    preds = [1, 0, 1, 1]; ys = [1, 1, 1, 0]
    print("zero_one(1,1) :", zero_one_loss(1, 1))
    print("zero_one(1,0) :", zero_one_loss(1, 0))
    print("empirical_risk:", empirical_risk(preds, ys))
    print("gap(0.3,0.5)  :", generalisation_gap(0.3, 0.5))


if __name__ == "__main__":
    main()
