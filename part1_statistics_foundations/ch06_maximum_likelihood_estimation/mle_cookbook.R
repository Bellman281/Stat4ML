# MLE cookbook -- maximum-likelihood estimators for the common distributions.
# Chapter 6, Part I.  A reference gallery, not a graded exercise. Base R only.
#   Rscript mle_cookbook.R
# Each estimator solves the likelihood equation l'(theta)=0 (ch06_text.tex,
# Section 1); the last one shows the numeric recipe for families with no
# closed form.

mle_bernoulli   <- function(x)     mean(x)                     # p
mle_binomial    <- function(x, k)  mean(x) / k                 # p, k known
mle_geometric   <- function(x)     length(x) / sum(x)          # p, support 1,2,...
mle_poisson     <- function(x)     mean(x)                     # lambda
mle_exponential <- function(x)     length(x) / sum(x)          # rate lambda
mle_normal      <- function(x)     c(mu = mean(x),
                                     var = sum((x - mean(x))^2) / length(x))
mle_uniform     <- function(x)     max(x)                      # theta of U(0, theta)
mle_laplace     <- function(x) { mu <- median(x); c(mu = mu, b = mean(abs(x - mu))) }
mle_pareto      <- function(x, xm) length(x) / sum(log(x / xm))  # alpha
mle_gamma_scale <- function(x, k)  mean(x) / k                 # theta, shape k known

# no closed form: generic Newton solver for l'(theta)=0
mle_newton <- function(score, hess, init, iters = 50) {
  theta <- init
  for (i in seq_len(iters)) theta <- theta - score(theta) / hess(theta)
  theta
}
mle_exponential_numeric <- function(x, init = 1.0) {
  n <- length(x); s <- sum(x)
  mle_newton(function(L) n / L - s, function(L) -n / L^2, init)
}

demo <- function() {
  cat("Bernoulli  p    :", mle_bernoulli(c(1, 1, 0, 1, 0)), "\n")
  cat("Binomial   p    :", mle_binomial(c(3, 5, 4, 6, 2), k = 10), "\n")
  cat("Geometric  p    :", mle_geometric(c(1, 2, 1, 4, 3, 1)), "\n")
  cat("Poisson    lam  :", mle_poisson(c(2, 1, 3, 0, 2, 1, 4, 2)), "\n")
  cat("Exponential lam :", mle_exponential(c(0.4, 1.2, 0.9, 2.1)), "\n")
  cat("Normal   mu,s2  :", mle_normal(c(2, 4, 4, 4, 5, 5, 7, 9)), "\n")
  cat("Uniform   theta :", mle_uniform(c(0.2, 0.9, 0.5, 0.8)), "\n")
  cat("Laplace  mu,b   :", mle_laplace(c(1, 2, 2, 3, 10)), "\n")
  cat("Pareto   alpha  :", mle_pareto(c(2, 3, 5, 8), xm = 1), "\n")
  cat("Gamma    theta  :", mle_gamma_scale(c(2, 4, 6, 8), k = 2), "\n")
  cat("Exp (Newton)    :", mle_exponential_numeric(c(0.4, 1.2, 0.9, 2.1)), "\n")
}

demo()
