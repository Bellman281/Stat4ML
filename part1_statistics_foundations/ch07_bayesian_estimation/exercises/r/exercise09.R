# Chapter 7 exercise -- Conjugacy, prediction, Bernstein-von Mises (Research tier)
# level: research
# HOMEWORK: ch07_text.tex Sections 1 and 3.  Rscript exercise09.R

gamma_poisson_posterior <- function(a, b, total, n) {
  # TODO: c(a + total, b + n)
  stop("TODO: gamma_poisson_posterior")
}
posterior_predictive_next_success <- function(alpha, beta) {
  # TODO: alpha / (alpha + beta)
  stop("TODO: posterior_predictive_next_success")
}
bvm_posterior_sd <- function(fisher_info_n) {
  # TODO: 1 / sqrt(fisher_info_n)
  stop("TODO: bvm_posterior_sd")
}

main <- function() {
  cat("gamma-poisson post :", gamma_poisson_posterior(2, 1, 30, 10), "\n")
  cat("predictive success :", posterior_predictive_next_success(9, 3), "\n")
  cat("BvM posterior sd   :", bvm_posterior_sd(100), "\n")
}
main()
