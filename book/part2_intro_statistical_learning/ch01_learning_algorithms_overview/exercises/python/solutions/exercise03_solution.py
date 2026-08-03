"""Reference solution for exercise03.py (Chapter 1, Part II, Exercise 3)."""


def online_variance_update(state, new_x):
    n, mean, m2 = state
    n = n + 1
    delta = new_x - mean
    mean = mean + delta / n
    delta2 = new_x - mean
    m2 = m2 + delta * delta2
    return (n, mean, m2)


def variance_from_state(state):
    n, _mean, m2 = state
    return m2 / n if n > 0 else 0.0


def pseudo_label_accuracy(teacher_preds, true_labels):
    matches = sum(1 for p, t in zip(teacher_preds, true_labels) if p == t)
    return matches / len(true_labels)


def semi_supervised_combined_accuracy(labeled_acc, labeled_frac, pseudo_acc, unlabeled_frac):
    return labeled_frac * labeled_acc + unlabeled_frac * pseudo_acc


def main():
    stream = [4.0, 6.0, 8.0, 2.0, 10.0]
    state = (0, 0.0, 0.0)
    for x in stream:
        state = online_variance_update(state, x)
    var = variance_from_state(state)
    print(f"online variance of {stream} = {var}  (expect 8.0)")

    teacher_preds = [1, 0, 1, 1, 0]
    true_labels = [1, 0, 0, 1, 0]
    acc = pseudo_label_accuracy(teacher_preds, true_labels)
    print(f"pseudo_label_accuracy = {acc}  (expect 0.8)")

    combined = semi_supervised_combined_accuracy(0.95, 0.1, acc, 0.9)
    print(f"semi_supervised_combined_accuracy = {combined:.4f}")


if __name__ == "__main__":
    main()
