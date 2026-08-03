"""
Chapter 0 exercise 1 -- Matrix Algebra Review: core operations
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using only ch00_text.tex Sections 1-4
(matrix multiplication, determinants, the inverse, transpose).

Run with:  python3 exercise01.py
Reference solution: solutions/exercise01_solution.py
"""


def matmul(A, B):
    """C = AB. A is n x k, B is k x m (lists of lists of floats);
    returns the n x m product. See ch00_text.tex Definition 1.1."""
    # TODO
    raise NotImplementedError("TODO: matmul")


def transpose(A):
    """A^T: swap rows and columns of A (a list of lists)."""
    # TODO
    raise NotImplementedError("TODO: transpose")


def det2x2(A):
    """det(A) = ad - bc for A = [[a, b], [c, d]]. See ch00_text.tex
    Section 2."""
    # TODO
    raise NotImplementedError("TODO: det2x2")


def inverse2x2(A):
    """A^-1 = (1/det A) * [[d, -b], [-c, a]] for A = [[a, b], [c, d]].
    See ch00_text.tex Section 3. Assume det(A) != 0."""
    # TODO
    raise NotImplementedError("TODO: inverse2x2")


def identity2x2():
    return [[1.0, 0.0], [0.0, 1.0]]


def main():
    A = [[1.0, 2.0], [3.0, 4.0]]
    B = [[5.0, 6.0], [7.0, 8.0]]

    AB = matmul(A, B)
    print(f"AB = {AB}")

    lhs = transpose(AB)
    rhs = matmul(transpose(B), transpose(A))
    print(f"(AB)^T = {lhs}, B^T A^T = {rhs}  -- should match (Theorem 4.1)")

    dA, dB, dAB = det2x2(A), det2x2(B), det2x2(AB)
    print(f"det(A)*det(B) = {dA * dB}, det(AB) = {dAB}  -- should match (Theorem 2.1.8)")

    invA = inverse2x2(A)
    check = matmul(A, invA)
    print(f"A @ A^-1 = {check}  -- should be the 2x2 identity")


if __name__ == "__main__":
    main()
