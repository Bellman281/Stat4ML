# Chapter 10 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (nonconformity, coverage).

nonconformity <- function(y, pred) {
  # BUG: the nonconformity score is the ABSOLUTE residual |y - pred|.
  y - pred
}
quantile_rank <- function(n, alpha) ceiling((n + 1) * (1 - alpha))
coverage <- function(ys, preds, q) {
  # BUG: a point is covered when its nonconformity is <= q, not > q.
  mean(abs(ys - preds) > q)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("nonconformity", nonconformity(3.0, 2.5), 0.5)
  check("nonconformity_neg", nonconformity(2.0, 3.0), 1.0)
  check("quantile_rank", quantile_rank(99, 0.1), 90)
  check("coverage", coverage(c(1.0, 2.0, 3.0), c(1.0, 2.0, 5.0), 1.0), 2.0 / 3.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
