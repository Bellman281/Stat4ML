# Chapter 3 -- reference solution (Proof, R)
# level: proof
ridge_estimator_1d <- function(x, y, lam) {
  sxy <- sum((x - mean(x)) * (y - mean(y))); sxx <- sum((x - mean(x))^2)
  sxy / (sxx + lam)
}
soft_threshold <- function(z, lam) {
  if (z > lam) z - lam else if (z < -lam) z + lam else 0
}
sigmoid_prime <- function(z) { s <- 1 / (1 + exp(-z)); s * (1 - s) }
main <- function() {
  x <- c(1, 2, 3); y <- c(2, 4, 6)
  cat("ridge (lam=2)     :", ridge_estimator_1d(x, y, 2.0), "\n")
  cat("soft_threshold    :", soft_threshold(-2.0, 1.0), "\n")
  cat("sigmoid_prime(0)  :", sigmoid_prime(0.0), "\n")
}
main()
