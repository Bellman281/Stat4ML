# Chapter 0 exercise 2 -- Matrix Algebra Review: LU decomposition
# Part I: Statistics Foundation for ML
#
# HOMEWORK: implement each TODO using Doolittle's method for a 2x2
# matrix, as worked out in ch00_text.tex Section 6.1 (Matrix
# Decompositions).
#
# Run with:  Rscript exercise02.R
# Reference solution: solutions/exercise02_solution.R

matmul <- function(A, B) {
  n <- nrow(A); k <- ncol(A); m <- ncol(B)
  C <- matrix(0, nrow = n, ncol = m)
  for (i in 1:n) for (j in 1:m) {
    s <- 0
    for (t in 1:k) s <- s + A[i, t] * B[t, j]
    C[i, j] <- s
  }
  C
}

lu_decompose_2x2 <- function(A) {
  # TODO: Doolittle's method.
  #   u11 = a11, u12 = a12
  #   l21 = a21 / a11
  #   u22 = a22 - l21 * u12
  # Return list(L = ..., U = ...). See ch00_text.tex Section 6.1 (and
  # its editorial note on the "u11=14" typo -- don't reproduce it here).
  stop("TODO: lu_decompose_2x2")
}

reconstruct <- function(L, U) {
  # TODO: L %*% U (using your matmul, not the builtin operator).
  stop("TODO: reconstruct")
}

main <- function() {
  A <- matrix(c(4, 3, 6, 3), nrow = 2, byrow = TRUE)  # same example as ch00_text.tex
  lu <- lu_decompose_2x2(A)
  cat("L =\n"); print(lu$L)
  cat("U =\n"); print(lu$U)
  A_check <- reconstruct(lu$L, lu$U)
  cat("L @ U =\n"); print(A_check)
  cat("A =\n"); print(A)
}

main()
