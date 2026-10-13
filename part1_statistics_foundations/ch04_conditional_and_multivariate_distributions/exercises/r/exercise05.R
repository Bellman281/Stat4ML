# Chapter 4 exercise -- Total expectation and total variance (Proof tier)
# level: proof
# Groups Y=1..k with within-group means, within-group variances, weights.
# Rscript exercise05.R

group_mean <- function(means, weights) {
  # TODO: sum(weights * means)
  stop("TODO: group_mean")
}
within_var <- function(vars, weights) {
  # TODO: sum(weights * vars)
  stop("TODO: within_var")
}
between_var <- function(means, weights) {
  # TODO: sum(weights * means^2) - (sum(weights * means))^2
  stop("TODO: between_var")
}
total_variance <- function(vars, means, weights) {
  # TODO: within_var + between_var
  stop("TODO: total_variance")
}

main <- function() {
  w <- c(0.5, 0.5); m <- c(0.0, 10.0); v <- c(1.0, 1.0)
  cat("E[X]        :", group_mean(m, w), "\n")
  cat("within var  :", within_var(v, w), "\n")
  cat("between var :", between_var(m, w), "\n")
  cat("total var   :", total_variance(v, m, w), "\n")
}
main()
