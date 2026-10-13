# Chapter 2 -- reference solution (Core, R)
# level: core
ols_slope <- function(x, y) sum((x - mean(x)) * (y - mean(y))) / sum((x - mean(x))^2)
ols_intercept <- function(x, y) mean(y) - ols_slope(x, y) * mean(x)
predict_lin <- function(b0, b1, x) b0 + b1 * x
r_squared <- function(x, y, b0, b1) {
  ss_res <- sum((y - (b0 + b1 * x))^2); ss_tot <- sum((y - mean(y))^2)
  1 - ss_res / ss_tot
}
main <- function() {
  x <- c(0, 1, 2, 3); y <- c(1, 3, 5, 7)
  b1 <- ols_slope(x, y); b0 <- ols_intercept(x, y)
  cat("slope, intercept :", b1, b0, "\n")
  cat("predict at 10    :", predict_lin(b0, b1, 10), "\n")
  cat("R^2              :", r_squared(x, y, b0, b1), "\n")
}
main()
