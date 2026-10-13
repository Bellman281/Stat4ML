# Chapter 6 -- reference solution (Core, R)
# level: core

bernoulli_loglik <- function(p, data) sum(data * log(p) + (1 - data) * log(1 - p))

bernoulli_mle <- function(data) mean(data)

poisson_mle <- function(data) mean(data)

normal_mle <- function(data) {
  n <- length(data)
  mu <- sum(data) / n
  sigma2 <- sum((data - mu)^2) / n
  c(mu, sigma2)
}

main <- function() {
  b <- c(1, 1, 0, 1, 0, 1, 0, 0, 1, 1)
  cat(sprintf("Bernoulli MLE p_hat = %s\n", bernoulli_mle(b)))
  cat(sprintf("log-lik at 0.6     = %.4f\n", bernoulli_loglik(0.6, b)))
  cat(sprintf("Poisson MLE        = %s\n", poisson_mle(c(2,1,3,0,2,1,4,2))))
  nm <- normal_mle(c(2,4,4,4,5,5,7,9))
  cat(sprintf("Normal MLE mu=%s sigma2=%s\n", nm[1], nm[2]))
}

main()
