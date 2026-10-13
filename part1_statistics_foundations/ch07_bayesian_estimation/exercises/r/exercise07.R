# Chapter 7 exercise -- Beta-Binomial updating (Core)
# level: core
# HOMEWORK: ch07_text.tex Section 1.  Rscript exercise07.R

beta_binomial_posterior <- function(alpha, beta, k, n) {
  # TODO: c(alpha + k, beta + n - k)
  stop("TODO: beta_binomial_posterior")
}
posterior_mean <- function(alpha, beta) {
  # TODO: alpha / (alpha + beta)
  stop("TODO: posterior_mean")
}
beta_map <- function(alpha, beta) {
  # TODO: (alpha - 1) / (alpha + beta - 2)
  stop("TODO: beta_map")
}

main <- function() {
  post <- beta_binomial_posterior(1, 1, 8, 10)
  cat("posterior params :", post, "\n")
  cat("posterior mean   :", posterior_mean(post[1], post[2]), "\n")
  cat("MAP estimate     :", beta_map(post[1], post[2]), "\n")
}
main()
