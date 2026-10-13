# Chapter 4 -- reference solution (Proof, R)
# level: proof
group_mean <- function(means, weights) sum(weights * means)
within_var <- function(vars, weights) sum(weights * vars)
between_var <- function(means, weights) sum(weights * means^2) - (sum(weights * means))^2
total_variance <- function(vars, means, weights) within_var(vars, weights) + between_var(means, weights)
main <- function() {
  w <- c(0.5, 0.5); m <- c(0.0, 10.0); v <- c(1.0, 1.0)
  cat("E[X]        :", group_mean(m, w), "\n")
  cat("within var  :", within_var(v, w), "\n")
  cat("between var :", between_var(m, w), "\n")
  cat("total var   :", total_variance(v, m, w), "\n")
}
main()
