# Chapter 10 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (conformal_q, empirical_coverage).

conformal_q <- function(cal_scores, alpha) {
  n <- length(cal_scores)
  # BUG: the rank rounds UP (ceiling); floor can pick too small a threshold.
  k <- floor((n + 1) * (1 - alpha))
  if (k > n) return(Inf)
  sort(cal_scores)[k]
}
empirical_coverage <- function(test_scores, q) {
  # BUG: a score is covered when it is <= q, not >= q.
  mean(test_scores >= q)
}
guarantee_holds <- function(cov, alpha) cov >= 1 - alpha - 1e-9

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- if (is.logical(expected)) identical(got, expected) else isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  cal <- c(0.2, 0.4, 0.6, 0.8, 1.0)
  check("conformal_q", conformal_q(cal, 0.2), 1.0)
  test <- c(0.5, 0.9, 1.5, 0.1, 0.7)
  check("empirical_coverage", empirical_coverage(test, 1.0), 0.8)
  check("guarantee_holds", guarantee_holds(empirical_coverage(test, 1.0), 0.2), TRUE)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
