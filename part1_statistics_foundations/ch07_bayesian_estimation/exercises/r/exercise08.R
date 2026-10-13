# Chapter 7 exercise -- Normal-Normal conjugacy (Proof tier)
# level: proof
# HOMEWORK: ch07_text.tex Section 2.  Rscript exercise08.R

normal_posterior_precision <- function(tau2, sigma2, n) {
  # TODO: 1/tau2 + n/sigma2
  stop("TODO: normal_posterior_precision")
}
normal_posterior_mean <- function(mu0, tau2, xbar, sigma2, n) {
  # TODO: (mu0/tau2 + n*xbar/sigma2) / precision
  stop("TODO: normal_posterior_mean")
}
normal_posterior_var <- function(tau2, sigma2, n) {
  # TODO: 1 / precision
  stop("TODO: normal_posterior_var")
}

main <- function() {
  cat("precision :", normal_posterior_precision(1.0, 1.0, 10), "\n")
  cat("mean      :", normal_posterior_mean(0.0, 1.0, 2.0, 1.0, 10), "\n")
  cat("variance  :", normal_posterior_var(1.0, 1.0, 10), "\n")
}
main()
