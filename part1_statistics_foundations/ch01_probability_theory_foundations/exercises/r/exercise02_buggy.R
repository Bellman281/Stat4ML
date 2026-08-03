# Chapter 1 -- RUSTLINGS-STYLE EXERCISE (R edition), Exercise 2
# Part I: Statistics Foundation for ML
#
# Three deliberate bugs are hiding below (in pmf_three_coins,
# cdf_three_coins, and inverse_transform_sample). Run this file, read
# the first failing check, fix ONLY that function, and re-run -- repeat
# until you see "All tests passed!". Do not edit run_tests().
#
# Run with:  Rscript exercise02_buggy.R

pmf_three_coins <- function(x) {
  # BUG: forgets the binomial coefficient C(3,x) -- returns (1/2)^3 for
  # every x (see ch01_text.tex Section 5, three-fair-coins example).
  0.5^3
}

cdf_three_coins <- function(x) {
  # BUG: uses strict "<" instead of "<=" -- an off-by-one that
  # under-counts at integer boundaries (see ch01_text.tex Section 6.1).
  k <- floor(x)
  total <- 0
  for (i in 0:3) if (i < k) total <- total + pmf_three_coins(i)
  total
}

inverse_transform_sample <- function(u) {
  # BUG: missing the leading minus sign -- ch01_text.tex Section 8
  # derives Y = -log(X), not log(X).
  log(u)
}

exponential_pdf <- function(y) {
  # Correct (not part of this exercise).
  if (y >= 0) exp(-y) else 0.0
}

# ---------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# ---------------------------------------------------------------------------
run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    status <- if (ok) "PASS" else "FAIL"
    cat(sprintf("[%s] %s: got=%s expected=%s\n", status, name, got, expected))
    if (!ok) failures <<- c(failures, name)
  }

  check("pmf_three_coins(0)", pmf_three_coins(0), 1 / 8)
  check("pmf_three_coins(1)", pmf_three_coins(1), 3 / 8)
  check("pmf sums to 1", sum(sapply(0:3, pmf_three_coins)), 1.0)

  check("cdf_three_coins(2.5)", cdf_three_coins(2.5), 7 / 8)
  check("cdf_three_coins(-1)", cdf_three_coins(-1), 0.0)
  check("cdf_three_coins(3.5)", cdf_three_coins(3.5), 1.0)

  set.seed(7)
  n <- 200000
  u <- pmax(runif(n), 1e-12)
  samples <- sapply(u, inverse_transform_sample)
  check("mean of inverse-transform samples ~ 1.0 (Exponential(1))", round(mean(samples), 1), 1.0, tol = 0.15)

  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED: %s\n", length(failures), paste(failures, collapse = ", ")))
    quit(status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
