# Chapter 00: Matrix Algebra Review

_Part I -- Statistics Foundation for ML_

**Status:** complete -- written chapter, plus three exercises in each of
Python and R with a broken copy of each to fix.

Matrix algebra was originally handed out as a prerequisite slide deck,
`PreReq1_Matrix_Calculus.pdf`. It is written out here as a full chapter
with its own homework, because almost everything downstream leans on it:
the partitioned-matrix notation in Chapter 2 (Moments), the normal
equations in Part II's regression chapter, PCA's eigendecomposition, and
backpropagation's Jacobians.

## Contents

- `ch00_text.tex` / `ch00_text.pdf` -- the chapter text
- `figures/` -- chapter figures
- `source_slides/PreReq1_Matrix_Calculus.pdf` -- the original prerequisite
  slide deck, exactly as handed out
- `exercises/python/`, `exercises/r/` -- three homework
  exercises, each with a **broken** copy for you to debug and a reference
  solution, in each of the two languages

## Topics

- Matrix multiplication
- Determinants (2x2 formula + general properties)
- The inverse matrix
- Matrix transpose
- Partitioned matrices
- Eigenvalues and eigenvectors
- Matrix decompositions: LU, Cholesky, QR, SVD
- Matrix differentiation (including the derivative of a matrix inverse)

## Exercises

1. **Core operations** -- matrix multiplication, transpose, and the 2x2
   determinant/inverse formulas; verifies `(AB)^T = B^T A^T` and
   `det(AB) = det(A) det(B)`.
2. **LU decomposition** -- Doolittle's method for a 2x2 matrix, verified
   by reconstructing `A = LU`.
3. **Eigenvalues and eigenvectors** -- the 2x2 characteristic
   polynomial, verified against the trace/determinant identities.

## Corrections to the original slides

Two bugs found in the original `PreReq1_Matrix_Calculus.pdf` slides are
called out directly in `ch00_text.tex`, with the correct derivation
alongside: a digit typo in a worked LU-decomposition example (`u11`
should equal `a11`, not a stray "14"), and a missing leading minus sign
in the derivative-of-a-matrix-inverse identity.

## Source

Original slide deck preserved at
`source_slides/PreReq1_Matrix_Calculus.pdf`.
