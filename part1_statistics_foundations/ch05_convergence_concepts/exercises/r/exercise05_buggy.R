# Chapter 5 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (var_of_sample_mean, chebyshev_bound).

var_of_sample_mean <- function(sigma2, n) {
  # BUG: variance of the sample mean is sigma^2 / n, not sigma^2 * n.
  sigma2 * n
}
chebyshev_bound <- function(sigma2, n, eps) {
  # BUG: Chebyshev divides by eps SQUARED, not eps.
  sigma2 / (n * eps)
}
running_mean <- function(data) cumsum(data) / seq_along(data)
clt_standardized <- function(xbar, mu, sigma, n) (xbar - mu) / (sigma / sqrt(n))

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("var_of_sample_mean", var_of_sample_mean(4.0, 100), 0.04)
  check("chebyshev_bound", chebyshev_bound(4.0, 100, 0.5), 4.0 / (100 * 0.25))
  rm <- running_mean(c(2, 4, 6))
  check("running_mean first", rm[1], 2.0)
  check("running_mean last", rm[length(rm)], 4.0)
  check("clt_standardized", clt_standardized(1.6, 1.0, 2.0, 100), 3.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
