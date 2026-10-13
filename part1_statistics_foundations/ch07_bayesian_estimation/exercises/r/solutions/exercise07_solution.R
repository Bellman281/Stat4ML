# Chapter 7 -- reference solution (Core, R)
# level: core
beta_binomial_posterior <- function(alpha, beta, k, n) c(alpha + k, beta + n - k)
posterior_mean <- function(alpha, beta) alpha / (alpha + beta)
beta_map <- function(alpha, beta) (alpha - 1) / (alpha + beta - 2)
main <- function() {
  post <- beta_binomial_posterior(1, 1, 8, 10)
  cat("posterior params :", post, "\n")
  cat("posterior mean   :", posterior_mean(post[1], post[2]), "\n")
  cat("MAP estimate     :", beta_map(post[1], post[2]), "\n")
}
main()
