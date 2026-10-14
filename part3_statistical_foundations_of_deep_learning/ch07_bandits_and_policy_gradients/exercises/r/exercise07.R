# Chapter 7 exercise -- bandit action selection (Core tier)
# level: core
# HOMEWORK: ch07_text.tex Section 1.  Rscript exercise07.R
# NOTE: R indices are 1-based, so argmax_index returns a 1-based index.

ucb_index <- function(mean, n, t, c) {
  # TODO: mean + sqrt(c * log(t) / n)
  stop("TODO: ucb_index")
}
argmax_index <- function(values) {
  # TODO: index (1-based) of the maximum; use which.max
  stop("TODO: argmax_index")
}
cumulative_regret <- function(mu_star, chosen_means) {
  # TODO: sum(mu_star - chosen_means)
  stop("TODO: cumulative_regret")
}

main <- function() {
  cat("ucb_index         :", ucb_index(0.5, 4, 100, 2.0), "\n")
  cat("argmax_index      :", argmax_index(c(1.0, 5.0, 3.0)), "\n")
  cat("cumulative_regret :", cumulative_regret(1.0, c(0.8, 0.9, 1.0)), "\n")
}
main()
