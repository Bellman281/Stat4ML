"""Chapter 5 -- reference solution (Proof)."""
# level: proof
import math


def matvec2(S, w):
    return [S[0][0] * w[0] + S[0][1] * w[1],
            S[1][0] * w[0] + S[1][1] * w[1]]


def projected_variance(S, w):
    Sw = matvec2(S, w)
    return w[0] * Sw[0] + w[1] * Sw[1]


def top_eigenvalue_2x2(S):
    tr = S[0][0] + S[1][1]
    det = S[0][0] * S[1][1] - S[0][1] * S[1][0]
    return (tr + math.sqrt(tr * tr - 4 * det)) / 2


def main():
    S = [[2.0, 0.8], [0.8, 0.6]]
    print("matvec2       :", matvec2([[2, 0], [0, 1]], [1, 0]))
    print("proj variance :", projected_variance([[2, 0], [0, 1]], [0.6, 0.8]))
    print("top eigenvalue:", top_eigenvalue_2x2(S))


if __name__ == "__main__":
    main()
