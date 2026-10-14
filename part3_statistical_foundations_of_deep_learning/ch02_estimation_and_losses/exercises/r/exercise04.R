# Chapter 2 exercise -- the score function (Research tier)
# level: research
# HOMEWORK: ch02_text.tex Section 3.  Rscript exercise04.R

gaussian_score <- function(y, mu, sigma2) {
  # TODO: (y - mu) / sigma2
  stop("TODO: gaussian_score")
}
bernoulli_score <- function(y, p) {
  # TODO: (y - p) / (p * (1 - p))
  stop("TODO: bernoulli_score")
}
mle_mean <- function(ys) {
  # TODO: the mu solving sum (y - mu) = 0, i.e. the mean
  stop("TODO: mle_mean")
}

main <- function() {
  ys <- c(2.0, 4.0, 6.0)
  cat("gaussian_score :", gaussian_score(3.0, 1.0, 2.0), "\n")
  cat("bernoulli_score:", bernoulli_score(1, 0.5), "\n")
  mu <- mle_mean(ys)
  cat("mle_mean       :", mu, "\n")
  cat("total score@mle:", sum(sapply(ys, function(y) gaussian_score(y, mu, 1.0))), "\n")
}
main()
