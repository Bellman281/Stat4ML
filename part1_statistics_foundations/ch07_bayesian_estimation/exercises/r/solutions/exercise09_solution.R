# Chapter 7 -- reference solution (Research, R)
# level: research
gamma_poisson_posterior <- function(a, b, total, n) c(a + total, b + n)
posterior_predictive_next_success <- function(alpha, beta) alpha / (alpha + beta)
bvm_posterior_sd <- function(fisher_info_n) 1 / sqrt(fisher_info_n)
main <- function() {
  cat("gamma-poisson post :", gamma_poisson_posterior(2, 1, 30, 10), "\n")
  cat("predictive success :", posterior_predictive_next_success(9, 3), "\n")
  cat("BvM posterior sd   :", bvm_posterior_sd(100), "\n")
}
main()
