# Chapter 1 (Part II) -- RUSTLINGS-STYLE EXERCISE (R edition)
#
# Four deliberate bugs are hiding below (in simple_linear_regression_fit,
# predict_line, mse, and kmeans_assign). Run this file, read the first
# failing check, fix ONLY that function, and re-run -- repeat until you
# see "All tests passed!". Do not edit run_tests().
#
# Run with:  Rscript exercise01_buggy.R

simple_linear_regression_fit <- function(xs, ys) {
  # BUG: uses raw sums instead of centering around the means -- gives the
  # wrong line whenever xbar != 0.
  b1 <- sum(xs * ys) / sum(xs * xs)
  b0 <- mean(ys) - b1 * mean(xs)
  c(b0, b1)
}

predict_line <- function(xs, b0, b1) {
  # BUG: forgets the intercept term entirely.
  b1 * xs
}

mse <- function(y_true, y_pred) {
  # BUG: computes mean ABSOLUTE error, not mean SQUARED error.
  mean(abs(y_true - y_pred))
}

kmeans_assign <- function(points, centroids) {
  # BUG: only compares the x-coordinate (column 1), ignoring y entirely.
  n <- nrow(points)
  k <- nrow(centroids)
  assignments <- integer(n)
  for (i in seq_len(n)) {
    dists <- abs(points[i, 1] - centroids[, 1])
    assignments[i] <- which.min(dists)
  }
  assignments
}

online_mean_update <- function(old_mean, new_x, n) {
  # Correct.
  old_mean + (new_x - old_mean) / n
}

# ---------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# ---------------------------------------------------------------------------
run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- if (length(got) == length(expected)) all(abs(got - expected) < tol) else FALSE
    status <- if (ok) "PASS" else "FAIL"
    cat(sprintf("[%s] %s: got=%s expected=%s\n", status, name,
                paste(round(got, 4), collapse = ","), paste(expected, collapse = ",")))
    if (!ok) failures <<- c(failures, name)
  }

  # y = 1 + 2x exactly, NOT centered at x=0 (xbar=3) -- the buggy formula
  # gets this wrong.
  xs <- c(1, 2, 3, 4, 5)
  ys <- c(3, 5, 7, 9, 11)
  fit <- simple_linear_regression_fit(xs, ys)
  check("simple_linear_regression_fit", fit, c(1.0, 2.0))

  check("predict_line(c(0,1,2), b0=1, b1=2)", predict_line(c(0, 1, 2), 1.0, 2.0), c(1, 3, 5))

  check("mse(c(1,2,3), c(1,2,5))", mse(c(1, 2, 3), c(1, 2, 5)), 4 / 3)

  points <- matrix(c(0.0, 0.0, 0.2, 0.1, 0.0, 5.0, 0.1, 5.1), ncol = 2, byrow = TRUE)
  centroids <- matrix(c(0.0, 0.0, 0.0, 5.0), ncol = 2, byrow = TRUE)
  # x-coordinates of both centroids are 0 -- an x-only distance can't
  # distinguish them, so this exposes the bug.
  check("kmeans_assign (needs both coordinates)", kmeans_assign(points, centroids), c(1, 1, 2, 2))

  check("online_mean_update", online_mean_update(5.0, 15.0, 2), 10.0)

  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED: %s\n", length(failures), paste(failures, collapse = ", ")))
    quit(status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
