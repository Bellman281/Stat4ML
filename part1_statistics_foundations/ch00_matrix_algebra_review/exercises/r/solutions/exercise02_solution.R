# Reference solution for exercise02.R (Chapter 0, Exercise 2)

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
  a11 <- A[1, 1]; a12 <- A[1, 2]; a21 <- A[2, 1]; a22 <- A[2, 2]
  u11 <- a11; u12 <- a12
  l21 <- a21 / a11
  u22 <- a22 - l21 * u12
  L <- matrix(c(1, 0, l21, 1), nrow = 2, byrow = TRUE)
  U <- matrix(c(u11, u12, 0, u22), nrow = 2, byrow = TRUE)
  list(L = L, U = U)
}

reconstruct <- function(L, U) {
  matmul(L, U)
}

main <- function() {
  A <- matrix(c(4, 3, 6, 3), nrow = 2, byrow = TRUE)
  lu <- lu_decompose_2x2(A)
  cat("L =\n"); print(lu$L)
  cat("U =\n"); print(lu$U)
  A_check <- reconstruct(lu$L, lu$U)
  cat("L @ U =\n"); print(A_check)
  cat("A =\n"); print(A)
}

main()
