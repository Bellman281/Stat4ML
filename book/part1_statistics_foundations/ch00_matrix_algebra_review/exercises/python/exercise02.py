"""
Chapter 0 exercise 2 -- Matrix Algebra Review: LU decomposition
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using Doolittle's method for a 2x2 matrix,
as worked out in ch00_text.tex Section 6.1 (Matrix Decompositions).

Run with:  python3 exercise02.py
Reference solution: solutions/exercise02_solution.py
"""


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def lu_decompose_2x2(A):
    """Doolittle's method: A = LU with L unit-lower-triangular
    (l11=l22=1) and U upper-triangular. For A = [[a11,a12],[a21,a22]]:
      u11 = a11,  u12 = a12
      l21 = a21 / a11
      u22 = a22 - l21 * u12
    Returns (L, U) as 2x2 lists of lists. See ch00_text.tex Section 6.1
    (and its editorial note on the "u11=14" typo in the source slides --
    make sure you don't reproduce that typo here)."""
    # TODO
    raise NotImplementedError("TODO: lu_decompose_2x2")


def reconstruct(L, U):
    """L @ U -- should reproduce the original A exactly."""
    # TODO
    raise NotImplementedError("TODO: reconstruct")


def main():
    A = [[4.0, 3.0], [6.0, 3.0]]  # same example worked in ch00_text.tex
    L, U = lu_decompose_2x2(A)
    print(f"L = {L}")
    print(f"U = {U}")
    A_check = reconstruct(L, U)
    print(f"L @ U = {A_check}  -- should equal A = {A}")


if __name__ == "__main__":
    main()
