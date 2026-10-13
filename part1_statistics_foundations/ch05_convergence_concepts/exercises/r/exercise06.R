# Chapter 5 exercise -- Markov, Chebyshev, WLLN (Proof tier)
# level: proof
# HOMEWORK: implement each TODO using ch05_text.tex Section 2.  Rscript exercise06.R

markov_bound <- function(mean_nonneg, a) {
  # TODO: for Y >= 0, P(Y >= a) <= E[Y] / a
  stop("TODO: markov_bound")
}
chebyshev_bound <- function(var, eps) {
  # TODO: P(|X-mu| >= eps) <= var / eps^2
  stop("TODO: chebyshev_bound")
}
empirical_tail <- function(samples, mu, eps) {
  # TODO: fraction of samples with |x - mu| >= eps
  stop("TODO: empirical_tail")
}
wlln_bound <- function(sigma2, n, eps) {
  # TODO: sigma^2 / (n * eps^2)
  stop("TODO: wlln_bound")
}

main <- function() {
  data <- c(1, 2, 2, 2, 3, 2, 2, 2, 2, 10)
  cat("Markov(E=2, a=8)      :", markov_bound(2.0, 8), "\n")
  cat("Chebyshev(var=1, e=2) :", chebyshev_bound(1.0, 2.0), "\n")
  cat("empirical tail        :", empirical_tail(data, 2, 5), "\n")
  cat("WLLN bound n=100      :", wlln_bound(4.0, 100, 0.5), "\n")
}
main()
