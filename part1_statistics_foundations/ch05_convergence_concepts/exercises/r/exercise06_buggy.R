# Chapter 5 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (markov_bound, chebyshev_bound).

markov_bound <- function(mean_nonneg, a) {
  # BUG: Markov is E[Y]/a, not a/E[Y].
  a / mean_nonneg
}
chebyshev_bound <- function(var, eps) {
  # BUG: Chebyshev divides by eps SQUARED, not eps.
  var / eps
}
empirical_tail <- function(samples, mu, eps) mean(abs(samples - mu) >= eps)
wlln_bound <- function(sigma2, n, eps) sigma2 / (n * eps^2)

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  data <- c(1, 2, 2, 2, 3, 2, 2, 2, 2, 10)
  check("markov_bound", markov_bound(2.0, 8), 0.25)
  check("chebyshev_bound", chebyshev_bound(1.0, 2.0), 0.25)
  check("empirical_tail", empirical_tail(data, 2, 5), 0.1)
  check("wlln_bound n=100", wlln_bound(4.0, 100, 0.5), 0.16)
  check("wlln_bound n=400", wlln_bound(4.0, 400, 0.5), 0.04)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
