# Chapter 4 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (gaussian_kl, elbo).

gaussian_kl <- function(mu, sigma2) {
  # BUG: the KL has -log(sigma2), not +log(sigma2).
  0.5 * (sigma2 + mu^2 - 1 + log(sigma2))
}
mc_expectation <- function(samples) mean(samples)
elbo <- function(recon_loglik, mu, sigma2) {
  # BUG: the ELBO SUBTRACTS the KL (reconstruction minus KL), not adds it.
  recon_loglik + gaussian_kl(mu, sigma2)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("kl_prior_equals_prior", gaussian_kl(0.0, 1.0), 0.0)
  check("kl_shifted", gaussian_kl(1.0, 1.0), 0.5)
  check("kl_scaled", gaussian_kl(0.0, 2.0), 0.5 * (2 - 1 - log(2)))
  check("mc_expectation", mc_expectation(c(-2.0, -1.0, -3.0)), -2.0)
  check("elbo", elbo(-2.0, 1.0, 1.0), -2.0 - 0.5)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
