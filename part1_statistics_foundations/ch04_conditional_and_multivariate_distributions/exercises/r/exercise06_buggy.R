# Chapter 4 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (bvn_conditional_mean, bvn_conditional_var).

bvn_conditional_mean <- function(mu_y, rho, sy, sx, x, mu_x) {
  # BUG: the slope is rho * sy/sx, not rho * sx/sy.
  mu_y + rho * (sx / sy) * (x - mu_x)
}
bvn_conditional_var <- function(sy, rho) {
  # BUG: the conditional variance scales sy SQUARED, not sy.
  sy * (1 - rho^2)
}
mvn_conditional_mean_1d <- function(mu1, s12, s22, x2, mu2) mu1 + (s12 / s22) * (x2 - mu2)

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("bvn_conditional_mean", bvn_conditional_mean(0.0, 0.7, 2.0, 1.0, 2.0, 0.0), 2.8)
  check("bvn_conditional_var", bvn_conditional_var(2.0, 0.7), 4.0 * (1 - 0.49))
  check("mvn_conditional_mean_1d", mvn_conditional_mean_1d(0.0, 0.7, 1.0, 2.0, 0.0), 1.4)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
