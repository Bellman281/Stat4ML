# Chapter 4 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (importance_weight, eff_sample_size).

importance_weight <- function(px, qx) {
  # BUG: the weight is p/q (target over proposal), not q/p.
  qx / px
}
is_estimate <- function(fvals, pxs, qxs) mean(fvals * pxs / qxs)
eff_sample_size <- function(weights) {
  # BUG: ESS is (sum w)^2 / sum(w^2); the numerator must be squared.
  sum(weights) / sum(weights^2)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("importance_weight", importance_weight(0.1, 0.2), 0.5)
  check("is_estimate", is_estimate(c(1, 1), c(0.2, 0.2), c(0.4, 0.4)), 0.5)
  check("ess_uniform", eff_sample_size(c(1, 1, 1, 1)), 4.0)
  check("ess_degenerate", eff_sample_size(c(2, 0, 0, 0)), 1.0)
  f <- c(1, 3, 5); p <- c(0.3, 0.3, 0.3)
  check("q=p reduces to MC", is_estimate(f, p, p), mean(f))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
