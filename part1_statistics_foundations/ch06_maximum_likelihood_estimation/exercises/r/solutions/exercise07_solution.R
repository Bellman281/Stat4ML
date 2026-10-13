# Chapter 6 -- reference solution (Proof, R)
# level: proof

score_bernoulli <- function(p, data) sum(data / p - (1 - data) / (1 - p))

fisher_information_bernoulli <- function(p, n) n / (p * (1 - p))

cramer_rao_lower_bound <- function(p, n) p * (1 - p) / n

mle_variance_sim <- function(p, n, reps, seed = 0) {
  set.seed(seed)
  est <- replicate(reps, mean(rbinom(n, 1, p)))
  m <- mean(est)
  sum((est - m)^2) / reps
}

main <- function() {
  data <- c(rep(1, 15), rep(0, 35))
  cat(sprintf("score at MLE p=0.3 : %.6f\n", score_bernoulli(0.3, data)))
  cat(sprintf("Fisher info(0.3,50): %.4f\n", fisher_information_bernoulli(0.3, 50)))
  cat(sprintf("CRLB(0.3,50)       : %.6f\n", cramer_rao_lower_bound(0.3, 50)))
  cat(sprintf("sim var of MLE     : %.6f\n", mle_variance_sim(0.3, 50, 20000, seed = 0)))
}

main()
