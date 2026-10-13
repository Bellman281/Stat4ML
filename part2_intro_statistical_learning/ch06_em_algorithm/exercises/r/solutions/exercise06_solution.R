# Chapter 6 -- reference solution (Core, R)
# level: core
gaussian_pdf <- function(x, mu, s2) exp(-(x - mu)^2 / (2 * s2)) / sqrt(2 * pi * s2)
responsibility <- function(x, pis, mus, s2s, k) {
  w <- sapply(seq_along(pis), function(j) pis[j] * gaussian_pdf(x, mus[j], s2s[j]))
  w[k] / sum(w)
}
weighted_mean <- function(xs, resps) sum(resps * xs) / sum(resps)
main <- function() {
  cat("gaussian_pdf(0,0,1) :", gaussian_pdf(0, 0, 1), "\n")
  cat("responsibility      :", responsibility(0, c(0.5, 0.5), c(-1, 1), c(1, 1), 1), "\n")
  cat("weighted_mean       :", weighted_mean(c(1, 2, 3), c(1, 1, 0)), "\n")
}
main()
