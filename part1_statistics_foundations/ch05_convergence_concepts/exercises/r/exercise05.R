# Chapter 5 exercise -- Convergence (Core)
# Part I: Statistics Foundation for ML
# level: core
#
# HOMEWORK: implement each TODO using ch05_text.tex Section 1. Base R only.
#   Rscript exercise05.R

var_of_sample_mean <- function(sigma2, n) {
  # TODO: sigma^2 / n
  stop("TODO: var_of_sample_mean")
}
chebyshev_bound <- function(sigma2, n, eps) {
  # TODO: sigma^2 / (n * eps^2)
  stop("TODO: chebyshev_bound")
}
running_mean <- function(data) {
  # TODO: cumulative means, cumsum(data) / seq_along(data)
  stop("TODO: running_mean")
}
clt_standardized <- function(xbar, mu, sigma, n) {
  # TODO: (xbar - mu) / (sigma / sqrt(n))
  stop("TODO: clt_standardized")
}

main <- function() {
  cat("Var(Xbar) sigma2=4,n=100 :", var_of_sample_mean(4.0, 100), "\n")
  cat("Chebyshev bound          :", chebyshev_bound(4.0, 100, 0.5), "\n")
  cat("running mean of c(2,4,6) :", running_mean(c(2, 4, 6)), "\n")
  cat("standardized(1.6,1,2,100):", clt_standardized(1.6, 1.0, 2.0, 100), "\n")
}
main()
