# Reference solution for exercise03.R (Chapter 2, Exercise 3)

var_sum_two <- function(a, b, var_x, var_y, cov_xy) {
  a * a * var_x + b * b * var_y + 2 * a * b * cov_xy
}

cov_matrix_2x2 <- function(var_x, var_y, cov_xy) {
  matrix(c(var_x, cov_xy, cov_xy, var_y), nrow = 2, byrow = TRUE)
}

matvec <- function(M, v) {
  c(M[1, 1] * v[1] + M[1, 2] * v[2], M[2, 1] * v[1] + M[2, 2] * v[2])
}

var_linear_combo <- function(a_vec, cov_matrix) {
  sv <- matvec(cov_matrix, a_vec)
  a_vec[1] * sv[1] + a_vec[2] * sv[2]
}

matmul2x2 <- function(A, B) {
  C <- matrix(0, nrow = 2, ncol = 2)
  for (i in 1:2) for (j in 1:2) for (k in 1:2) C[i, j] <- C[i, j] + A[i, k] * B[k, j]
  C
}

transform_covariance <- function(R, sigma) {
  matmul2x2(matmul2x2(R, sigma), t(R))
}

main <- function() {
  var_x <- 2.0; var_y <- 3.0; cov_xy <- 0.5
  a <- 1.5; b <- -2.0

  direct <- var_sum_two(a, b, var_x, var_y, cov_xy)
  cat(sprintf("Var(aX+bY) directly = %g\n", direct))

  sigma <- cov_matrix_2x2(var_x, var_y, cov_xy)
  cat("Cov(X) =\n"); print(sigma)
  via_matrix <- var_linear_combo(c(a, b), sigma)
  cat(sprintf("a^T Sigma a = %g  -- should match the direct formula above\n", via_matrix))

  R <- matrix(c(1, 0, 1, 1), nrow = 2, byrow = TRUE)
  result <- transform_covariance(R, sigma)
  cat("R Sigma R^T =\n"); print(result)
}

main()
