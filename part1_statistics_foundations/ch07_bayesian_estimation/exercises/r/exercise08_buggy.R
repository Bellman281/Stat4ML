# Chapter 7 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (normal_posterior_mean, normal_posterior_var).

normal_posterior_precision <- function(tau2, sigma2, n) 1 / tau2 + n / sigma2
normal_posterior_mean <- function(mu0, tau2, xbar, sigma2, n) {
  # BUG: the weighted sum must be divided by the posterior precision.
  mu0 / tau2 + n * xbar / sigma2
}
normal_posterior_var <- function(tau2, sigma2, n) {
  # BUG: the variance is 1 / precision, not the precision itself.
  normal_posterior_precision(tau2, sigma2, n)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("precision", normal_posterior_precision(1.0, 1.0, 10), 11.0)
  check("mean", normal_posterior_mean(0.0, 1.0, 2.0, 1.0, 10), 20.0 / 11.0)
  check("variance", normal_posterior_var(1.0, 1.0, 10), 1.0 / 11.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
