# Chapter 2 -- reference solution (Core, R)
# level: core
mse <- function(preds, targets) mean((preds - targets)^2)
bernoulli_nll <- function(p, y) -(y * log(p) + (1 - y) * log(1 - p))
gaussian_nll <- function(mu, ys, sigma) {
  n <- length(ys)
  n / 2 * log(2 * pi * sigma^2) + sum((ys - mu)^2) / (2 * sigma^2)
}
main <- function() {
  cat("mse           :", mse(c(1, 2, 3), c(1, 2, 5)), "\n")
  cat("bernoulli_nll :", bernoulli_nll(0.8, 1), "\n")
  cat("gaussian_nll  :", gaussian_nll(0.0, c(1.0, -1.0), 2.0), "\n")
}
main()
