# Chapter 9 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (gp_post_mean, gp_post_var).

gp_post_mean <- function(k_star, k_11, sigma2, y) {
  # BUG: the denominator includes the noise (k_11 + sigma2); this omits it.
  k_star / k_11 * y
}
gp_post_var <- function(k_ss, k_star, k_11, sigma2) {
  # BUG: the predictive variance SUBTRACTS the reduction term; this adds it.
  k_ss + k_star^2 / (k_11 + sigma2)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("gp_post_mean", gp_post_mean(0.6, 1.0, 0.1, 2.0), 0.6 / 1.1 * 2.0)
  check("gp_post_var", gp_post_var(1.0, 0.6, 1.0, 0.1), 1.0 - 0.36 / 1.1)
  check("var_at_data_is_zero", gp_post_var(1.0, 1.0, 1.0, 0.0), 0.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
