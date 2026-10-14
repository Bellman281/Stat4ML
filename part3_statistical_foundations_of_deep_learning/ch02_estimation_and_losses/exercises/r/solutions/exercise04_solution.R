# Chapter 2 -- reference solution (Research, R)
# level: research
gaussian_score <- function(y, mu, sigma2) (y - mu) / sigma2
bernoulli_score <- function(y, p) (y - p) / (p * (1 - p))
mle_mean <- function(ys) sum(ys) / length(ys)
main <- function() {
  ys <- c(2.0, 4.0, 6.0)
  cat("gaussian_score :", gaussian_score(3.0, 1.0, 2.0), "\n")
  cat("bernoulli_score:", bernoulli_score(1, 0.5), "\n")
  mu <- mle_mean(ys)
  cat("mle_mean       :", mu, "\n")
  cat("total score@mle:", sum(sapply(ys, function(y) gaussian_score(y, mu, 1.0))), "\n")
}
main()
