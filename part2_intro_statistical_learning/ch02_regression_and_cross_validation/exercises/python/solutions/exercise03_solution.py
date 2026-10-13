"""Chapter 2 -- reference solution (Proof)."""
# level: proof
def squared_bias(preds, truth):
    m = sum(preds) / len(preds)
    return (m - truth) ** 2


def estimator_variance(preds):
    m = sum(preds) / len(preds)
    return sum((p - m) ** 2 for p in preds) / len(preds)


def expected_mse(preds, truth):
    return sum((p - truth) ** 2 for p in preds) / len(preds)


def main():
    preds, truth = [2.0, 4.0, 6.0], 5.0
    print("bias^2   :", squared_bias(preds, truth))
    print("variance :", estimator_variance(preds))
    print("MSE      :", expected_mse(preds, truth))


if __name__ == "__main__":
    main()
