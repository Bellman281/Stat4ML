# Chapter 2 exercise 4 -- MGF derivatives give moments
# Part I: Statistics Foundation for ML
#
# HOMEWORK: implement each TODO using only ch02_text.tex Section 3
# (moment generating functions, and E[X^n] = M_X^(n)(0)) and the Normal
# MGF formula. Use central finite differences:
#   M'(0)  ~= (M(h) - M(-h)) / (2h)
#   M''(0) ~= (M(h) - 2 M(0) + M(-h)) / h^2
#
# Run with:  Rscript exercise04.R
# Reference solution: solutions/exercise04_solution.R

mgf_normal <- function(t, mu, sigma2) {
  # Provided for you.
  exp(mu * t + sigma2 * t^2 / 2.0)
}

first_derivative_at_zero <- function(mu, sigma2, h) {
  # TODO
  stop("TODO: first_derivative_at_zero")
}

second_derivative_at_zero <- function(mu, sigma2, h) {
  # TODO
  stop("TODO: second_derivative_at_zero")
}

variance_from_derivatives <- function(mu, sigma2, h) {
  # TODO: Var(X) = E[X^2] - (E[X])^2.
  stop("TODO: variance_from_derivatives")
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
