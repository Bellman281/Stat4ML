# Chapter 5 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (entropy, kl).

entropy <- function(p) {
  # BUG: entropy is the NEGATIVE sum of p log p; the minus sign is missing.
  sum(p * log(p))
}
cross_entropy <- function(p, q) -sum(p * log(q))
kl <- function(p, q) {
  # BUG: KL(p||q) uses log(p/q), not log(q/p).
  sum(p * log(q / p))
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  p <- c(0.5, 0.5); q <- c(0.25, 0.75)
  check("entropy", entropy(p), log(2))
  check("cross_entropy", cross_entropy(p, q), -(0.5 * log(0.25) + 0.5 * log(0.75)))
  check("kl", kl(p, q), 0.5 * log(0.5 / 0.25) + 0.5 * log(0.5 / 0.75))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
