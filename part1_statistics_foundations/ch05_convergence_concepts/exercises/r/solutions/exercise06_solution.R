# Chapter 5 -- reference solution (Proof, R)
# level: proof
markov_bound <- function(mean_nonneg, a) mean_nonneg / a
chebyshev_bound <- function(var, eps) var / eps^2
empirical_tail <- function(samples, mu, eps) mean(abs(samples - mu) >= eps)
wlln_bound <- function(sigma2, n, eps) sigma2 / (n * eps^2)

main <- function() {
  data <- c(1, 2, 2, 2, 3, 2, 2, 2, 2, 10)
  cat("Markov(E=2, a=8)      :", markov_bound(2.0, 8), "\n")
  cat("Chebyshev(var=1, e=2) :", chebyshev_bound(1.0, 2.0), "\n")
  cat("empirical tail        :", empirical_tail(data, 2, 5), "\n")
  cat("WLLN bound n=100      :", wlln_bound(4.0, 100, 0.5), "\n")
}
main()
