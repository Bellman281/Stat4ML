# Chapter 1 -- RUSTLINGS-STYLE EXERCISE (R edition), Exercise 3
# Part I: Statistics Foundation for ML
#
# Three deliberate bugs are hiding below (in independence_check,
# exponential_cdf, and probability_integral_transform_mean). Run this
# file, read the first failing check, fix ONLY that function, and
# re-run -- repeat until you see "All tests passed!". Do not edit
# run_tests().
#
# Run with:  Rscript exercise03_buggy.R

independence_check <- function(p_a, p_b, p_a_and_b, tol = 1e-9) {
  # BUG: checks the disjoint-events additivity condition instead of the
  # independence condition -- see ch01_text.tex Section 4.
  abs(p_a_and_b - (p_a + p_b)) < tol
}

intersection_with_complement <- function(p_a, p_b_and_a) {
  # Correct.
  p_a - p_b_and_a
}

exponential_cdf <- function(y) {
  # BUG: returns the density e^{-y} instead of integrating it to get
  # the CDF 1 - e^{-y}.
  if (y >= 0) exp(-y) else 0.0
}

probability_integral_transform_mean <- function(n, seed = 0) {
  # BUG: forgets to apply exponential_cdf -- averages the raw
  # Exponential(1) samples, converging to 1.0 instead of 0.5.
  set.seed(seed)
  u <- pmax(runif(n), 1e-12)
  x <- -log(u)
  mean(x)
}

# ---------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# ---------------------------------------------------------------------------
run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- if (is.logical(expected)) (got == expected) else (abs(got - expected) < tol)
    status <- if (ok) "PASS" else "FAIL"
    cat(sprintf("[%s] %s: got=%s expected=%s\n", status, name, got, expected))
    if (!ok) failures <<- c(failures, name)
  }

  check("independence_check(0.5,0.4,0.2) TRUE", independence_check(0.5, 0.4, 0.2), TRUE)
  check("independence_check(0.5,0.4,0.3) FALSE", independence_check(0.5, 0.4, 0.3), FALSE)

  check("intersection_with_complement(0.5,0.3)", intersection_with_complement(0.5, 0.3), 0.2)

  check("exponential_cdf(0)", exponential_cdf(0), 0.0)
  check("exponential_cdf(1)", round(exponential_cdf(1), 4), round(1 - exp(-1), 4))

  m <- probability_integral_transform_mean(200000, seed = 7)
  check("probability_integral_transform_mean ~ 0.5", round(m, 1), 0.5, tol = 0.15)

  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED: %s\n", length(failures), paste(failures, collapse = ", ")))
    quit(status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
