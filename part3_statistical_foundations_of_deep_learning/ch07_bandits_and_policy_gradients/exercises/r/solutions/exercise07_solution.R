# Chapter 7 -- reference solution (Core, R)
# level: core
ucb_index <- function(mean, n, t, c) mean + sqrt(c * log(t) / n)
argmax_index <- function(values) which.max(values)
cumulative_regret <- function(mu_star, chosen_means) sum(mu_star - chosen_means)
main <- function() {
  cat("ucb_index         :", ucb_index(0.5, 4, 100, 2.0), "\n")
  cat("argmax_index      :", argmax_index(c(1.0, 5.0, 3.0)), "\n")
  cat("cumulative_regret :", cumulative_regret(1.0, c(0.8, 0.9, 1.0)), "\n")
}
main()
