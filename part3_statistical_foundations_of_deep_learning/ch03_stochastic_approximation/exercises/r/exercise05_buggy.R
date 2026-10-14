# Chapter 3 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (ou_stationary_var, polyak_var).

ou_stationary_var <- function(lr, sigma2, H) {
  # BUG: the stationary variance is lr*sigma2 / (2H); the factor 2 is missing.
  lr * sigma2 / H
}
critical_lr <- function(H) 2 / H
polyak_var <- function(stationary_var, k) {
  # BUG: averaging k iterates DIVIDES the variance by k, not multiplies.
  stationary_var * k
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-12) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  v <- ou_stationary_var(0.1, 1.0, 2.0)
  check("ou_stationary_var", v, 0.025)
  check("critical_lr", critical_lr(2.0), 1.0)
  check("polyak_var", polyak_var(0.025, 10), 0.0025)
  check("linear in lr", ou_stationary_var(0.2, 1.0, 2.0), 2 * ou_stationary_var(0.1, 1.0, 2.0))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
