# Chapter 7 -- reference solution (Proof, R)
# level: proof
normal_posterior_precision <- function(tau2, sigma2, n) 1 / tau2 + n / sigma2
normal_posterior_mean <- function(mu0, tau2, xbar, sigma2, n) {
  prec <- normal_posterior_precision(tau2, sigma2, n)
  (mu0 / tau2 + n * xbar / sigma2) / prec
}
normal_posterior_var <- function(tau2, sigma2, n) 1 / normal_posterior_precision(tau2, sigma2, n)
main <- function() {
  cat("precision :", normal_posterior_precision(1.0, 1.0, 10), "\n")
  cat("mean      :", normal_posterior_mean(0.0, 1.0, 2.0, 1.0, 10), "\n")
  cat("variance  :", normal_posterior_var(1.0, 1.0, 10), "\n")
}
main()
