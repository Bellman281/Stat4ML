# Chapter 6 exercise -- M-estimation & the sandwich variance (Research tier)
# Part I: Statistics Foundation for ML
# level: research
#
# Working model: X ~ N(theta, 1). Implement each TODO using Section 3.
# Run with:  Rscript exercise08.R
# Reference solution: solutions/exercise08_solution.R

avg_negloglik <- function(theta, data) {
  # TODO: mean(0.5*(data-theta)^2 + 0.5*log(2*pi))
  stop("TODO: avg_negloglik")
}

fisher_scoring_mean <- function(data, init, iters) {
  # TODO: repeat theta <- theta + sum(data-theta)/length(data)
  stop("TODO: fisher_scoring_mean")
}

naive_variance <- function(data) {
  # TODO: 1/length(data)
  stop("TODO: naive_variance")
}

sandwich_variance <- function(data, theta) {
  # TODO: A <- length(data); B <- sum((data-theta)^2); B / A^2
  stop("TODO: sandwich_variance")
}

main <- function() {
  data <- c(1, 3, 2, 6, 4, 2, 5, 1)  # mean 3.0, spread > 1
  th <- fisher_scoring_mean(data, 0.0, 1)
  cat(sprintf("Fisher scoring theta = %s  (expect 3.0)\n", th))
  cat(sprintf("avg NLL at 3.0       = %.4f\n", avg_negloglik(3.0, data)))
  cat(sprintf("naive var (1/n)      = %s\n", naive_variance(data)))
  cat(sprintf("sandwich var         = %s  (>> naive if misspecified)\n", sandwich_variance(data, th)))
}

main()
