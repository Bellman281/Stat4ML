# Chapter 6 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (geometric_bound, num_iters_for_tol).

sup_norm <- function(v, u) max(abs(v - u))
geometric_bound <- function(init_err, gamma, k) {
  # BUG: the contraction compounds multiplicatively: gamma^k, not gamma*k.
  init_err * gamma * k
}
num_iters_for_tol <- function(init_err, gamma, tol) {
  if (init_err <= tol) return(0)
  # BUG: k must be rounded UP (ceiling); floor can leave error above tolerance.
  max(0, floor(log(tol / init_err) / log(gamma)))
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- if (is.logical(expected)) identical(got, expected) else isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("sup_norm", sup_norm(c(1.0, 2.0, 3.0), c(1.0, 2.0, 5.0)), 2.0)
  check("geometric_bound", geometric_bound(10.0, 0.9, 2), 8.1)
  k <- num_iters_for_tol(1.0, 0.9, 0.01)
  check("num_iters_for_tol", k, 44)
  check("bound met at k", 0.9^k <= 0.01 + 1e-12, TRUE)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
