# Chapter 6 -- reference solution (Research, R)
# level: research

avg_negloglik <- function(theta, data) mean(0.5 * (data - theta)^2 + 0.5 * log(2 * pi))

fisher_scoring_mean <- function(data, init, iters) {
  n <- length(data)
  theta <- init
  for (i in seq_len(iters)) theta <- theta + sum(data - theta) / n
  theta
}

naive_variance <- function(data) 1 / length(data)

sandwich_variance <- function(data, theta) {
  n <- length(data)
  B <- sum((data - theta)^2)
  B / (n^2)
}

main <- function() {
  data <- c(1, 3, 2, 6, 4, 2, 5, 1)
  th <- fisher_scoring_mean(data, 0.0, 1)
  cat(sprintf("Fisher scoring theta = %s\n", th))
  cat(sprintf("avg NLL at 3.0       = %.4f\n", avg_negloglik(3.0, data)))
  cat(sprintf("naive var (1/n)      = %s\n", naive_variance(data)))
  cat(sprintf("sandwich var         = %s\n", sandwich_variance(data, th)))
}

main()
