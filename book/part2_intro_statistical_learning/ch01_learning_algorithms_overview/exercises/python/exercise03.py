"""
Chapter 1 exercise 3 -- Online variance (Welford's algorithm) and
semi-supervised pseudo-label accuracy
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO. ch01_text.tex Section 4 (Online Learning)
gives the running-mean update; this exercise extends it to running
VARIANCE via Welford's algorithm, and separately implements a toy version
of the "teacher generates pseudo-labels" idea from Section 3
(Semi-Supervised Learning).

Run with:  python3 exercise03.py
Reference solution: solutions/exercise03_solution.py
"""


def online_variance_update(state, new_x):
    """One step of Welford's online algorithm. `state` is a
    (n, mean, M2) tuple; `new_x` is the next observation. Return the
    updated (n, mean, M2):
        n' = n + 1
        delta = new_x - mean
        mean' = mean + delta / n'
        delta2 = new_x - mean'   (deviation from the UPDATED mean)
        M2' = M2 + delta * delta2
    """
    # TODO
    raise NotImplementedError("TODO: online_variance_update")


def variance_from_state(state):
    """Population variance from a Welford (n, mean, M2) state:
    Var(X) = M2 / n (matches ch02_text.tex's Var(X) = E[(X-mu)^2]
    population definition; NOT the n-1 sample-variance correction)."""
    # TODO
    raise NotImplementedError("TODO: variance_from_state")


def pseudo_label_accuracy(teacher_preds, true_labels):
    """Fraction of teacher_preds that match true_labels (ch01_text.tex
    Section 3: a teacher model's predictions used as pseudo-labels)."""
    # TODO
    raise NotImplementedError("TODO: pseudo_label_accuracy")


def semi_supervised_combined_accuracy(labeled_acc, labeled_frac, pseudo_acc, unlabeled_frac):
    """Weighted blend of the small-labeled-set accuracy and the
    pseudo-labeled-set accuracy: labeled_frac*labeled_acc +
    unlabeled_frac*pseudo_acc. Provided for you -- not part of this
    exercise."""
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
