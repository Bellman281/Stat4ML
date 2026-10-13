# Chapter 7 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (beta_binomial_posterior, beta_map).

beta_binomial_posterior <- function(alpha, beta, k, n) {
  # BUG: the second parameter is beta + (n - k), not beta + n.
  c(alpha + k, beta + n)
}
posterior_mean <- function(alpha, beta) alpha / (alpha + beta)
beta_map <- function(alpha, beta) {
  # BUG: the mode numerator is (alpha - 1), not alpha.
  alpha / (alpha + beta - 2)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  post <- beta_binomial_posterior(1, 1, 8, 10)
  check("posterior alpha", post[1], 9)
  check("posterior beta", post[2], 3)
  check("posterior_mean", posterior_mean(9, 3), 0.75)
  check("beta_map", beta_map(9, 3), 0.8)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
