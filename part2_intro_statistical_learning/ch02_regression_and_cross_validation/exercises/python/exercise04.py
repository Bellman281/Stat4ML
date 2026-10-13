"""
Chapter 2 exercise -- Cross-validation (Research tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch02_text.tex Section 3 (k-fold sizes,
averaging fold errors, and the LOOCV leverage shortcut).

Run with:  python3 exercise04.py
Reference solution: solutions/exercise04_solution.py
"""
# level: research
def kfold_split_sizes(n, k):
    """Sizes of k folds that partition n points as evenly as possible; the
    first (n mod k) folds get one extra. The sizes must sum to n."""
    raise NotImplementedError("TODO: kfold_split_sizes")


def mean_cv_error(fold_errors):
    """Average of the per-fold errors."""
    raise NotImplementedError("TODO: mean_cv_error")


def loocv_from_leverage(residuals, leverages):
    """LOOCV error without refitting:
    mean( (e_i / (1 - h_i))^2 )  over all points."""
    raise NotImplementedError("TODO: loocv_from_leverage")


def main():
    print("fold sizes   :", kfold_split_sizes(10, 3))
    print("mean cv err  :", mean_cv_error([0.1, 0.2, 0.3]))
    print("loocv        :", loocv_from_leverage([1.0, 1.0], [0.5, 0.5]))


if __name__ == "__main__":
    main()
