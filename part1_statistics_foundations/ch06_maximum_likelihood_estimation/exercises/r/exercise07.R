# Chapter 6 exercise -- Score, Fisher Information, Cramer-Rao (Proof tier)
# Part I: Statistics Foundation for ML
# level: proof
#
# HOMEWORK: implement each TODO using ch06_text.tex Section 2.
# Run with:  Rscript exercise07.R
# Reference solution: solutions/exercise07_solution.R

score_bernoulli <- function(p, data) {
  # TODO: sum(data/p - (1-data)/(1-p))
  stop("TODO: score_bernoulli")
}

fisher_information_bernoulli <- function(p, n) {
  # TODO: n / (p*(1-p))
  stop("TODO: fisher_information_bernoulli")
}

cramer_rao_lower_bound <- function(p, n) {
  # TODO: p*(1-p)/n
  stop("TODO: cramer_rao_lower_bound")
}

mle_variance_sim <- function(p, n, reps, seed = 0) {
  # TODO: set.seed(seed); est <- replicate(reps, mean(rbinom(n, 1, p)));
  #       return population variance of est.
  stop("TODO: mle_variance_sim")
}

main <- function() {
  data <- c(rep(1, 15), rep(0, 35))  # MLE = 0.3
  cat(sprintf("score at MLE p=0.3 : %.6f  (expect ~0)\n", score_bernoulli(0.3, data)))
  cat(sprintf("Fisher info(0.3,50): %.4f\n", fisher_information_bernoulli(0.3, 50)))
  cat(sprintf("CRLB(0.3,50)       : %.6f\n", cramer_rao_lower_bound(0.3, 50)))
  cat(sprintf("sim var of MLE     : %.6f\n", mle_variance_sim(0.3, 50, 20000, seed = 0)))
}

main()
