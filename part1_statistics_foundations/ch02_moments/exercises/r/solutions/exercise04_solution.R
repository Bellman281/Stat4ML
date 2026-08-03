# Reference solution for exercise04.R (Chapter 2, Exercise 4)

mgf_normal <- function(t, mu, sigma2) {
  exp(mu * t + sigma2 * t^2 / 2.0)
}

first_derivative_at_zero <- function(mu, sigma2, h) {
  (mgf_normal(h, mu, sigma2) - mgf_normal(-h, mu, sigma2)) / (2 * h)
}

second_derivative_at_zero <- function(mu, sigma2, h) {
  m0 <- mgf_normal(0.0, mu, sigma2)
  (mgf_normal(h, mu, sigma2) - 2 * m0 + mgf_normal(-h, mu, sigma2)) / (h^2)
}

variance_from_derivatives <- function(mu, sigma2, h) {
  d1 <- first_derivative_at_zero(mu, sigma2, h)
  d2 <- second_derivative_at_zero(mu, sigma2, h)
  d2 - d1^2
}

main <- function() {
  mu <- 2.0; sigma2 <- 4.0; h <- 1e-4

  d1 <- first_derivative_at_zero(mu, sigma2, h)
  cat(sprintf("M_X'(0) ~= %.6f  (theoretical E[X] = mu = %g)\n", d1, mu))

  d2 <- second_derivative_at_zero(mu, sigma2, h)
  cat(sprintf("M_X''(0) ~= %.6f  (theoretical E[X^2] = sigma2+mu^2 = %g)\n", d2, sigma2 + mu^2))

  v <- variance_from_derivatives(mu, sigma2, h)
  cat(sprintf("Var(X) via derivatives ~= %.6f  (theoretical Var(X) = sigma2 = %g)\n", v, sigma2))
}

main()
