# Chapter 3 exercise -- Ridge, soft-threshold, convexity (Proof tier)
# level: proof
# HOMEWORK: ch03_text.tex Section 2.  Rscript exercise04.R

ridge_estimator_1d <- function(x, y, lam) {
  # TODO: Sxy / (Sxx + lam)
  stop("TODO: ridge_estimator_1d")
}
soft_threshold <- function(z, lam) {
  # TODO: sign(z) * max(|z| - lam, 0)
  stop("TODO: soft_threshold")
}
sigmoid_prime <- function(z) {
  # TODO: s*(1-s) with s = sigmoid(z)
  stop("TODO: sigmoid_prime")
}

main <- function() {
  x <- c(1, 2, 3); y <- c(2, 4, 6)
  cat("ridge (lam=2)     :", ridge_estimator_1d(x, y, 2.0), "\n")
  cat("soft_threshold    :", soft_threshold(-2.0, 1.0), "\n")
  cat("sigmoid_prime(0)  :", sigmoid_prime(0.0), "\n")
}
main()
