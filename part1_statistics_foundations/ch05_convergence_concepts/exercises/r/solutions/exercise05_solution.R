# Chapter 5 -- reference solution (Core, R)
# level: core
var_of_sample_mean <- function(sigma2, n) sigma2 / n
chebyshev_bound <- function(sigma2, n, eps) sigma2 / (n * eps^2)
running_mean <- function(data) cumsum(data) / seq_along(data)
clt_standardized <- function(xbar, mu, sigma, n) (xbar - mu) / (sigma / sqrt(n))

main <- function() {
  cat("Var(Xbar) sigma2=4,n=100 :", var_of_sample_mean(4.0, 100), "\n")
  cat("Chebyshev bound          :", chebyshev_bound(4.0, 100, 0.5), "\n")
  cat("running mean of c(2,4,6) :", running_mean(c(2, 4, 6)), "\n")
  cat("standardized(1.6,1,2,100):", clt_standardized(1.6, 1.0, 2.0, 100), "\n")
}
main()
