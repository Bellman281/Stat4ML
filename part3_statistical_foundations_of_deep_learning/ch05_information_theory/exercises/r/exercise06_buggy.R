# Chapter 5 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (identity_residual, log_bound_gap).

.entropy <- function(p) -sum(p * log(p))
.cross_entropy <- function(p, q) -sum(p * log(q))
.kl <- function(p, q) sum(p * log(p / q))

identity_residual <- function(p, q) {
  # BUG: the decomposition is H(p,q) = H(p) + KL, so the residual subtracts
  # entropy; this adds it.
  .cross_entropy(p, q) + .entropy(p) - .kl(p, q)
}
kl_is_nonneg <- function(p, q) .kl(p, q) >= -1e-12
log_bound_gap <- function(t) {
  # BUG: the bound is log t <= t - 1, so the gap is (t-1) - log t.
  log(t) - (t - 1)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- if (is.logical(expected)) identical(got, expected) else isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  p <- c(0.2, 0.3, 0.5); q <- c(0.3, 0.4, 0.3)
  check("identity_residual", identity_residual(p, q), 0.0)
  check("kl_is_nonneg", kl_is_nonneg(p, q), TRUE)
  check("log_bound_gap_1", log_bound_gap(1.0), 0.0)
  check("log_bound_gap_2", log_bound_gap(2.0), (2 - 1) - log(2))
  check("log_bound_gap_half", log_bound_gap(0.5), (0.5 - 1) - log(0.5))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
