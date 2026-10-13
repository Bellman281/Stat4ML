# Chapter 3 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (l1_penalty, elastic_net_penalty).

l1_penalty <- function(beta, lam) {
  # BUG: the L1 penalty sums ABSOLUTE values, not the raw coefficients.
  lam * sum(beta)
}
l2_penalty <- function(beta, lam) lam * sum(beta^2)
elastic_net_penalty <- function(beta, lam, alpha) {
  # BUG: alpha weights L1 and (1-alpha) weights L2; they're swapped here.
  lam * ((1 - alpha) * sum(abs(beta)) + alpha * sum(beta^2))
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  b <- c(1, -2, 3)
  check("l1_penalty", l1_penalty(b, 1.0), 6.0)
  check("l2_penalty", l2_penalty(b, 1.0), 14.0)
  check("elastic_net (alpha=0.25)", elastic_net_penalty(b, 1.0, 0.25), 12.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
