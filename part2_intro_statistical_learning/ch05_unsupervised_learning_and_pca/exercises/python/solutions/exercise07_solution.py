"""Chapter 5 -- reference solution (Research)."""
# level: research
import math


def cumulative_variance_explained(eigvals):
    total = sum(eigvals)
    out, run = [], 0.0
    for e in eigvals:
        run += e
        out.append(run / total)
    return out


def reconstruction_error_ratio(eigvals, k):
    return sum(eigvals[k:]) / sum(eigvals)


def singular_value_from_eigenvalue(eigval):
    return math.sqrt(eigval)


def main():
    print("cumulative    :", cumulative_variance_explained([4, 1]))
    print("recon error   :", reconstruction_error_ratio([4, 1], 1))
    print("singular value:", singular_value_from_eigenvalue(9))


if __name__ == "__main__":
    main()
