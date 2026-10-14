# Chapter 2 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (ridge_lambda, ridge_estimate_1d).

gaussian_log_prior <- function(w, tau) -w^2 / (2 * tau^2)
ridge_lambda <- function(sigma2, tau2) {
  # BUG: a N(0,tau^2) prior gives lam = sigma^2/tau^2, not tau^2/sigma^2.
  tau2 / sigma2
}
ridge_estimate_1d <- function(xs, ys, lam) {
  sxy <- sum(xs * ys); sxx <- sum(xs^2)
  # BUG: ridge ADDS lam to sum(x^2); subtracting it is wrong.
  sxy / (sxx - lam)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  xs <- c(1, 2, 3); ys <- c(2, 4, 6)
  check("gaussian_log_prior", gaussian_log_prior(2.0, 1.0), -2.0)
  check("ridge_lambda", ridge_lambda(1.0, 0.5), 2.0)
  check("ridge_ols", ridge_estimate_1d(xs, ys, 0.0), 2.0)
  lam <- 5.0
  J <- function(w) sum((ys - xs * w)^2) + lam * w^2
  grid <- seq(0, 4, by = 0.001)
  wgrid <- grid[which.min(sapply(grid, J))]
  check("MAP minimises objective", ridge_estimate_1d(xs, ys, lam), wgrid, tol = 2e-3)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
