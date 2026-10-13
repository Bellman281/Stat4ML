# Chapter 7 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (gamma_poisson_posterior, bvm_posterior_sd).

gamma_poisson_posterior <- function(a, b, total, n) {
  # BUG: the rate updates by n (number of observations), not the total count.
  c(a + total, b + total)
}
posterior_predictive_next_success <- function(alpha, beta) alpha / (alpha + beta)
bvm_posterior_sd <- function(fisher_info_n) {
  # BUG: the posterior sd is 1/sqrt(I_n); 1/I_n is the variance.
  1 / fisher_info_n
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  post <- gamma_poisson_posterior(2, 1, 30, 10)
  check("gamma-poisson shape", post[1], 32)
  check("gamma-poisson rate", post[2], 11)
  check("predictive success", posterior_predictive_next_success(9, 3), 0.75)
  check("BvM posterior sd", bvm_posterior_sd(100), 0.1)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
