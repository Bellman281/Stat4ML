# Chapter 2 -- RUSTLINGS-STYLE EXERCISE (R edition), Exercise 4
# Part I: Statistics Foundation for ML
#
# Three deliberate bugs are hiding below (in first_derivative_at_zero,
# second_derivative_at_zero, and variance_from_derivatives). Run this
# file, read the first failing check, fix ONLY that function, and
# re-run -- repeat until you see "All tests passed!". Do not edit
# run_tests().
#
# Run with:  Rscript exercise04_buggy.R

mgf_normal <- function(t, mu, sigma2) {
  # Correct.
  exp(mu * t + sigma2 * t^2 / 2.0)
}

first_derivative_at_zero <- function(mu, sigma2, h) {
  # BUG: forgets the factor of 2 in the denominator.
  (mgf_normal(h, mu, sigma2) - mgf_normal(-h, mu, sigma2)) / h
}

second_derivative_at_zero <- function(mu, sigma2, h) {
  # BUG: forgets the "-2*M(0)" term.
  (mgf_normal(h, mu, sigma2) + mgf_normal(-h, mu, sigma2)) / (h^2)
}

variance_from_derivatives <- function(mu, sigma2, h) {
  # BUG: forgets to subtract (E[X])^2.
  d2 <- second_derivative_at_zero(mu, sigma2, h)
  d2
}

# ---------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# ---------------------------------------------------------------------------
run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol) {
    ok <- abs(got - expected) < tol
    status <- if (ok) "PASS" else "FAIL"
    cat(sprintf("[%s] %s: got=%s expected=%s\n", status, name, got, expected))
    if (!ok) failures <<- c(failures, name)
  }

  mu <- 2.0; sigma2 <- 4.0; h <- 1e-4

  d1 <- first_derivative_at_zero(mu, sigma2, h)
  check("first_derivative_at_zero ~= mu", d1, mu, tol = 1e-3)

  d2 <- second_derivative_at_zero(mu, sigma2, h)
  check("second_derivative_at_zero ~= sigma2+mu^2", d2, sigma2 + mu^2, tol = 1e-2)

  v <- variance_from_derivatives(mu, sigma2, h)
  check("variance_from_derivatives ~= sigma2", v, sigma2, tol = 1e-2)

  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED: %s\n", length(failures), paste(failures, collapse = ", ")))
    quit(status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
