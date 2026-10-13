# Chapter 2 exercise -- Linear regression (Core)
# level: core
# HOMEWORK: ch02_text.tex Section 1.  Rscript exercise02.R

ols_slope <- function(x, y) {
  # TODO: sum((x-mean(x))*(y-mean(y))) / sum((x-mean(x))^2)
  stop("TODO: ols_slope")
}
ols_intercept <- function(x, y) {
  # TODO: mean(y) - slope * mean(x)
  stop("TODO: ols_intercept")
}
predict_lin <- function(b0, b1, x) {
  # TODO: b0 + b1 * x
  stop("TODO: predict_lin")
}
r_squared <- function(x, y, b0, b1) {
  # TODO: 1 - SS_res / SS_tot
  stop("TODO: r_squared")
}

main <- function() {
  x <- c(0, 1, 2, 3); y <- c(1, 3, 5, 7)
  b1 <- ols_slope(x, y); b0 <- ols_intercept(x, y)
  cat("slope, intercept :", b1, b0, "\n")
  cat("predict at 10    :", predict_lin(b0, b1, 10), "\n")
  cat("R^2              :", r_squared(x, y, b0, b1), "\n")
}
main()
