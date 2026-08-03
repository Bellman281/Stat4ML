# Chapter 0 exercise 3 -- Matrix Algebra Review: eigenvalues and eigenvectors
# Part I: Statistics Foundation for ML
#
# HOMEWORK: implement each TODO using the 2x2 characteristic-polynomial
# approach from ch00_text.tex Section 5 (Eigenvalues and Eigenvectors),
# lambda^2 - trace(A) lambda + det(A) = 0.
#
# Run with:  Rscript exercise03.R
# Reference solution: solutions/exercise03_solution.R

trace_ <- function(A) {
  # TODO: sum of the diagonal entries of A (NOT all four entries).
  stop("TODO: trace_")
}

det2x2 <- function(A) {
  A[1, 1] * A[2, 2] - A[1, 2] * A[2, 1]
}

eigenvalues_2x2 <- function(A) {
  # TODO: the two roots of lambda^2 - trace(A) lambda + det(A) = 0, via
  # the quadratic formula:
  #   lambda = (trace(A) +/- sqrt(trace(A)^2 - 4*det(A))) / 2
  # Return c(lambda1, lambda2) with lambda1 >= lambda2.
  stop("TODO: eigenvalues_2x2")
}

eigenvector_for_eigenvalue_2x2 <- function(A, lam) {
  # Provided for you -- not part of this exercise.
  a <- A[1, 1]; b <- A[1, 2]; c <- A[2, 1]; d <- A[2, 2]
  if (abs(b) > 1e-12) {
    v <- c(b, lam - a)
  } else {
    v <- c(lam - d, c)
  }
  v / sqrt(sum(v^2))
}

main <- function() {
  A <- matrix(c(0.8, 0.3, 0.2, 0.7), nrow = 2, byrow = TRUE)  # same example as ch00_text.tex
  lams <- eigenvalues_2x2(A)
  cat(sprintf("eigenvalues = %g, %g  (expect 1.0 and 0.5)\n", lams[1], lams[2]))
  cat(sprintf("trace(A) = %g, sum of eigenvalues = %g\n", trace_(A), sum(lams)))
  cat(sprintf("det(A) = %g, product of eigenvalues = %g\n", det2x2(A), prod(lams)))

  v1 <- eigenvector_for_eigenvalue_2x2(A, lams[1])
  Av1 <- c(A[1, 1] * v1[1] + A[1, 2] * v1[2], A[2, 1] * v1[1] + A[2, 2] * v1[2])
  cat("A @ v1 ="); print(Av1)
  cat("lambda1 * v1 ="); print(lams[1] * v1)
}

main()
