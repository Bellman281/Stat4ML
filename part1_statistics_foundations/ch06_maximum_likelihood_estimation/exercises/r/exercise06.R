# Chapter 6 exercise -- Maximum Likelihood Estimation (Core)
# Part I: Statistics Foundation for ML
# level: core
#
# HOMEWORK: implement each TODO using only ch06_text.tex Section 1 and base R.
# Run with:  Rscript exercise06.R
# Reference solution: solutions/exercise06_solution.R

bernoulli_loglik <- function(p, data) {
  # TODO: sum(data*log(p) + (1-data)*log(1-p))
  stop("TODO: bernoulli_loglik")
}

bernoulli_mle <- function(data) {
  # TODO: sample mean
  stop("TODO: bernoulli_mle")
}

poisson_mle <- function(data) {
  # TODO: sample mean
  stop("TODO: poisson_mle")
}

normal_mle <- function(data) {
  # TODO: c(mu, sigma2) with sigma2 dividing by n (NOT n-1)
  stop("TODO: normal_mle")
}

main <- function() {
  b <- c(1, 1, 0, 1, 0, 1, 0, 0, 1, 1)
  cat(sprintf("Bernoulli MLE p_hat = %s  (expect 0.6)\n", bernoulli_mle(b)))
  cat(sprintf("log-lik at 0.6     = %.4f\n", bernoulli_loglik(0.6, b)))
  cat(sprintf("Poisson MLE        = %s  (expect 1.875)\n", poisson_mle(c(2,1,3,0,2,1,4,2))))
  nm <- normal_mle(c(2,4,4,4,5,5,7,9))
  cat(sprintf("Normal MLE mu=%s sigma2=%s  (expect 5.0, 4.0)\n", nm[1], nm[2]))
}

main()
