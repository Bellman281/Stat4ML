# Chapter 2 -- RUSTLINGS-STYLE EXERCISE (R edition)
# Part I: Statistics Foundation for ML
#
# Four deliberate bugs are hiding below (in variance, correlation,
# normal_mgf_theoretical, and normal_mgf_monte_carlo). Run this file, read
# the first failing check, fix ONLY that function, and re-run -- repeat
# until you see "All tests passed!". Do not edit run_tests().
#
# Run with:  Rscript exercise02_buggy.R

expected_value <- function(values, probs) {
  # Correct.
  sum(values * probs)
}

variance <- function(values, probs) {
  # BUG: returns E[X^2] and forgets to subtract (E[X])^2.
  ex2 <- expected_value(values^2, probs)
  ex2
}

covariance <- function(x_values, y_values, joint_probs) {
  # Correct.
  ex <- sum(x_values * joint_probs)
  ey <- sum(y_values * joint_probs)
  exy <- sum(x_values * y_values * joint_probs)
  exy - ex * ey
}

correlation <- function(cov_xy, var_x, var_y) {
  # BUG: divides by the variances instead of the standard deviations.
  cov_xy / (var_x * var_y)
}

normal_mgf_theoretical <- function(t, mu, sigma2) {
  # BUG: missing "/2" in the exponent.
  exp(mu * t + sigma2 * t^2)
}

normal_mgf_monte_carlo <- function(t, mu, sigma2, n, seed = 0) {
  # BUG: forgets to scale by sqrt(sigma2) -- always samples sd=1.
  set.seed(seed)
  samples <- rnorm(n, mean = mu, sd = 1)
  mean(exp(t * samples))
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

  xs <- c(0, 1, 2, 3); ps <- c(1 / 8, 3 / 8, 3 / 8, 1 / 8)
  check("expected_value (Binomial(3,0.5))", expected_value(xs, ps), 1.5)
  check("variance (Binomial(3,0.5))", variance(xs, ps), 0.75)

  x_vals <- c(0, 0, 1, 1); y_vals <- c(0, 1, 0, 1); joint <- c(0.4, 0.1, 0.1, 0.4)
  check("covariance (positively associated)", covariance(x_vals, y_vals, joint), 0.15)

  check("correlation(cov=0.16, var_x=0.25, var_y=0.25)",
        correlation(0.16, 0.25, 0.25), 0.64)

  theo <- normal_mgf_theoretical(0.4, 2.0, 4.0)
  check("normal_mgf_theoretical(t=0.4, mu=2.0, sigma2=4.0)", round(theo, 5),
        round(exp(2.0 * 0.4 + 4.0 * 0.4^2 / 2.0), 5))

  mc <- normal_mgf_monte_carlo(0.4, 2.0, 4.0, 300000, seed = 7)
  expected_mc <- exp(2.0 * 0.4 + 4.0 * 0.4^2 / 2.0)
  check("normal_mgf_monte_carlo(t=0.4, mu=2.0, sigma2=4.0) ~ theoretical",
        round(mc, 1), round(expected_mc, 1), tol = 0.15)

  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED: %s\n", length(failures), paste(failures, collapse = ", ")))
    quit(status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
