# Chapter 2 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (ols_slope, r_squared).

ols_slope <- function(x, y) {
  # BUG: the slope uses centered sums Sxy/Sxx, not sum(x*y)/sum(x^2).
  sum(x * y) / sum(x * x)
}
ols_intercept <- function(x, y) mean(y) - ols_slope(x, y) * mean(x)
predict_lin <- function(b0, b1, x) b0 + b1 * x
r_squared <- function(x, y, b0, b1) {
  # BUG: R^2 is 1 - SS_res/SS_tot, not SS_res/SS_tot.
  ss_res <- sum((y - (b0 + b1 * x))^2); ss_tot <- sum((y - mean(y))^2)
  ss_res / ss_tot
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- length(got) == length(expected) && all(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, paste(format(got), collapse=","), paste(format(expected), collapse=",")))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  x <- c(0, 1, 2, 3); y <- c(1, 3, 5, 7)
  b1 <- ols_slope(x, y); b0 <- ols_intercept(x, y)
  check("ols_slope", b1, 2.0)
  check("ols_intercept", b0, 1.0)
  check("predict(10)", predict_lin(1.0, 2.0, 10), 21.0)
  check("r_squared", r_squared(x, y, 1.0, 2.0), 1.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
