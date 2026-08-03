# Chapter 2 -- RUSTLINGS-STYLE EXERCISE (R edition), Exercise 3
# Part I: Statistics Foundation for ML
#
# Three deliberate bugs are hiding below (in var_sum_two,
# cov_matrix_2x2, and transform_covariance). Run this file, read the
# first failing check, fix ONLY that function, and re-run -- repeat
# until you see "All tests passed!". Do not edit run_tests().
#
# Run with:  Rscript exercise03_buggy.R

var_sum_two <- function(a, b, var_x, var_y, cov_xy) {
  # BUG: forgets the cross term "2ab*Cov(X,Y)".
  a * a * var_x + b * b * var_y
}

cov_matrix_2x2 <- function(var_x, var_y, cov_xy) {
  # BUG: swaps the diagonal entries.
  matrix(c(var_y, cov_xy, cov_xy, var_x), nrow = 2, byrow = TRUE)
}

matvec <- function(M, v) {
  # Correct.
  c(M[1, 1] * v[1] + M[1, 2] * v[2], M[2, 1] * v[1] + M[2, 2] * v[2])
}

var_linear_combo <- function(a_vec, cov_matrix) {
  # Correct.
  sv <- matvec(cov_matrix, a_vec)
  a_vec[1] * sv[1] + a_vec[2] * sv[2]
}

matmul2x2 <- function(A, B) {
  C <- matrix(0, nrow = 2, ncol = 2)
  for (i in 1:2) for (j in 1:2) for (k in 1:2) C[i, j] <- C[i, j] + A[i, k] * B[k, j]
  C
}

transform_covariance <- function(R, sigma) {
  # BUG: forgets the trailing "%*% t(R))".
  matmul2x2(R, sigma)
}

# ---------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# ---------------------------------------------------------------------------
run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- all(abs(got - expected) < tol)
    status <- if (ok) "PASS" else "FAIL"
    cat(sprintf("[%s] %s\n", status, name))
    if (!ok) failures <<- c(failures, name)
  }

  var_x <- 2.0; var_y <- 3.0; cov_xy <- 0.5
  a <- 1.5; b <- -2.0

  direct <- var_sum_two(a, b, var_x, var_y, cov_xy)
  check("var_sum_two", direct, 13.5)

  sigma <- cov_matrix_2x2(var_x, var_y, cov_xy)
  check("cov_matrix_2x2", sigma, matrix(c(2, 0.5, 0.5, 3), nrow = 2, byrow = TRUE))

  via_matrix <- var_linear_combo(c(a, b), sigma)
  check("var_linear_combo matches var_sum_two", via_matrix, 13.5)

  R <- matrix(c(1, 0, 1, 1), nrow = 2, byrow = TRUE)
  result <- transform_covariance(R, sigma)
  check("transform_covariance", result, matrix(c(2, 2.5, 2.5, 6), nrow = 2, byrow = TRUE))

  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED: %s\n", length(failures), paste(failures, collapse = ", ")))
    quit(status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
