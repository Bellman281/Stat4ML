"""Chapter 2 -- reference solution (Research)."""
# level: research
def kfold_split_sizes(n, k):
    base, rem = n // k, n % k
    return [base + 1] * rem + [base] * (k - rem)


def mean_cv_error(fold_errors):
    return sum(fold_errors) / len(fold_errors)


def loocv_from_leverage(residuals, leverages):
    terms = [(e / (1 - h)) ** 2 for e, h in zip(residuals, leverages)]
    return sum(terms) / len(terms)


def main():
    print("fold sizes   :", kfold_split_sizes(10, 3))
    print("mean cv err  :", mean_cv_error([0.1, 0.2, 0.3]))
    print("loocv        :", loocv_from_leverage([1.0, 1.0], [0.5, 0.5]))


if __name__ == "__main__":
    main()
