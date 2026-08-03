# Reference solution for exercise03.R (Chapter 0, Exercise 3)

trace_ <- function(A) {
  A[1, 1] + A[2, 2]
}

det2x2 <- function(A) {
  A[1, 1] * A[2, 2] - A[1, 2] * A[2, 1]
}

eigenvalues_2x2 <- function(A) {
  tr <- trace_(A)
  d <- det2x2(A)
  disc <- sqrt(tr * tr - 4 * d)
  c((tr + disc) / 2, (tr - disc) / 2)
}

eigenvector_for_eigenvalue_2x2 <- function(A, lam) {
  a <- A[1, 1]; b <- A[1, 2]; c <- A[2, 1]; d <- A[2, 2]
  if (abs(b) > 1e-12) {
    v <- c(b, lam - a)
  } else {
    v <- c(lam - d, c)
  }
  v / sqrt(sum(v^2))
}

main <- function() {
  A <- matrix(c(0.8, 0.3, 0.2, 0.7), nrow = 2, byrow = TRUE)
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
