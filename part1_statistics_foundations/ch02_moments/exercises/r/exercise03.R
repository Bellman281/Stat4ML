# Chapter 2 exercise 3 -- Variance of linear combinations, matrix covariance
# Part I: Statistics Foundation for ML
#
# HOMEWORK: implement each TODO using only ch02_text.tex Section 2
# (Var(aX+bY)) and Section 4 (matrix notation for moments).
#
# Run with:  Rscript exercise03.R
# Reference solution: solutions/exercise03_solution.R

var_sum_two <- function(a, b, var_x, var_y, cov_xy) {
  # TODO: Var(aX+bY) = a^2 Var(X) + b^2 Var(Y) + 2ab Cov(X,Y).
  stop("TODO: var_sum_two")
}

cov_matrix_2x2 <- function(var_x, var_y, cov_xy) {
  # TODO: [[Var(X1), Cov(X1,X2)], [Cov(X1,X2), Var(X2)]].
  stop("TODO: cov_matrix_2x2")
}

matvec <- function(M, v) {
  # Provided for you.
  c(M[1, 1] * v[1] + M[1, 2] * v[2], M[2, 1] * v[1] + M[2, 2] * v[2])
}

var_linear_combo <- function(a_vec, cov_matrix) {
  # TODO: Var(a^T X) = a^T Sigma a.
  stop("TODO: var_linear_combo")
}

transform_covariance <- function(R, sigma) {
  # TODO: Var(RX) = R Sigma R^T.
  stop("TODO: transform_covariance")
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

  R <- matrix(c(1, 0, 1, 1), nrow = 2, byrow = TRUE)  # Y1=X1, Y2=X1+X2
  result <- transform_covariance(R, sigma)
  cat("R Sigma R^T =\n"); print(result)
}

main()
