# Chapter 00: Matrix Algebra Review

_Part I -- Statistics Foundation for ML_

**Status:** PILOT -- fully authored

This chapter did not exist in either source repo as its own chapter --
it is a new chapter written for this merged book, expanding
`PreReq1_Matrix_Calculus.pdf` (previously just a prerequisite slide deck
linked from the README) into a full O'Reilly-style chapter with its own
homework. Matrix algebra underlies almost everything downstream: the
partitioned-matrix notation in Chapter 2 (Moments), the normal-equations
solution in Part II's regression chapter, PCA's eigendecomposition, and
backpropagation's Jacobians all lean on the material here.

## Contents

- `ch00_text.tex` / `ch00_text.pdf` -- the chapter text
- `figures/` -- chapter figures
- `source_slides/PreReq1_Matrix_Calculus.pdf` -- original prerequisite
  slide deck, preserved unmodified
- `exercises/python/`, `exercises/r/`, `exercises/rust/` -- three
  homework exercises, each with a Rustlings-style **broken** exercise
  you must fix, and a reference solution, in each of the three languages

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

## Editorial notes

Two bugs found in the original `PreReq1_Matrix_Calculus.pdf` slides are
called out directly in `ch00_text.tex`, with the correct derivation
alongside: a digit typo in a worked LU-decomposition example (`u11`
should equal `a11`, not a stray "14"), and a missing leading minus sign
in the derivative-of-a-matrix-inverse identity.

## Source

Original slide deck preserved at
`source_slides/PreReq1_Matrix_Calculus.pdf`.
