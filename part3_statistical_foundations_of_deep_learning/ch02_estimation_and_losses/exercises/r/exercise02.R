# Chapter 2 exercise -- losses are negative log-likelihoods (Core tier)
# level: core
# HOMEWORK: ch02_text.tex Section 1.  Rscript exercise02.R

mse <- function(preds, targets) {
  # TODO: mean((preds - targets)^2)
  stop("TODO: mse")
}
bernoulli_nll <- function(p, y) {
  # TODO: -(y*log(p) + (1-y)*log(1-p))
  stop("TODO: bernoulli_nll")
}
gaussian_nll <- function(mu, ys, sigma) {
  # TODO: (n/2) log(2*pi*sigma^2) + sum((ys-mu)^2) / (2*sigma^2)
  stop("TODO: gaussian_nll")
}

main <- function() {
  cat("mse           :", mse(c(1, 2, 3), c(1, 2, 5)), "\n")
  cat("bernoulli_nll :", bernoulli_nll(0.8, 1), "\n")
  cat("gaussian_nll  :", gaussian_nll(0.0, c(1.0, -1.0), 2.0), "\n")
}
main()
