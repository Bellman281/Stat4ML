# Chapter 5 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (covariance, variance_explained_ratio).

center <- function(v) v - mean(v)
variance <- function(v) mean((v - mean(v))^2)
covariance <- function(x, y) {
  # BUG: covariance works on CENTERED values, not raw products.
  mean(x * y)
}
variance_explained_ratio <- function(eigvals) {
  # BUG: divide each eigenvalue by the SUM, not the max.
  eigvals / max(eigvals)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- length(got) == length(expected) && all(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, paste(format(got), collapse=","), paste(format(expected), collapse=",")))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("center", center(c(1, 2, 3)), c(-1, 0, 1))
  check("variance", variance(c(1, 2, 3)), 2/3)
  check("covariance", covariance(c(1, 2, 3), c(1, 2, 3)), 2/3)
  check("var ratio", variance_explained_ratio(c(3, 1)), c(0.75, 0.25))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
