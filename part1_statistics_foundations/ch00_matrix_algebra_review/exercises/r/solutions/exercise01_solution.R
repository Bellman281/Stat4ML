# Reference solution for exercise01.R (Chapter 0, Exercise 1)

matmul <- function(A, B) {
  n <- nrow(A); k <- ncol(A); m <- ncol(B)
  C <- matrix(0, nrow = n, ncol = m)
  for (i in 1:n) {
    for (j in 1:m) {
      s <- 0
      for (t in 1:k) s <- s + A[i, t] * B[t, j]
      C[i, j] <- s
    }
  }
  C
}

transpose <- function(A) {
  n <- nrow(A); m <- ncol(A)
  Tm <- matrix(0, nrow = m, ncol = n)
  for (i in 1:n) for (j in 1:m) Tm[j, i] <- A[i, j]
  Tm
}

det2x2 <- function(A) {
  A[1, 1] * A[2, 2] - A[1, 2] * A[2, 1]
}

inverse2x2 <- function(A) {
  d <- det2x2(A)
  matrix(c(A[2, 2] / d, -A[1, 2] / d, -A[2, 1] / d, A[1, 1] / d), nrow = 2, byrow = TRUE)
}

main <- function() {
  A <- matrix(c(1, 2, 3, 4), nrow = 2, byrow = TRUE)
  B <- matrix(c(5, 6, 7, 8), nrow = 2, byrow = TRUE)

  AB <- matmul(A, B)
  cat("AB =\n"); print(AB)

  lhs <- transpose(AB)
  rhs <- matmul(transpose(B), transpose(A))
  cat("(AB)^T =\n"); print(lhs)
  cat("B^T A^T =\n"); print(rhs)

  dA <- det2x2(A); dB <- det2x2(B); dAB <- det2x2(AB)
  cat(sprintf("det(A)*det(B) = %g, det(AB) = %g -- should match\n", dA * dB, dAB))

  invA <- inverse2x2(A)
  check <- matmul(A, invA)
  cat("A @ A^-1 =\n"); print(check)
}

main()
