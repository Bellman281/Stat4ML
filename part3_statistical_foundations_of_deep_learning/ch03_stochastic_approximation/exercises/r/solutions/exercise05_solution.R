# Chapter 3 -- reference solution (Research, R)
# level: research
ou_stationary_var <- function(lr, sigma2, H) lr * sigma2 / (2 * H)
critical_lr <- function(H) 2 / H
polyak_var <- function(stationary_var, k) stationary_var / k
main <- function() {
  v <- ou_stationary_var(0.1, 1.0, 2.0)
  cat("ou_stationary_var:", v, "\n")
  cat("critical_lr      :", critical_lr(2.0), "\n")
  cat("polyak_var (k=10):", polyak_var(v, 10), "\n")
}
main()
