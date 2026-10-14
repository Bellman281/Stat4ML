# Chapter 4 -- reference solution (Core, R)
# level: core
mc_estimate <- function(fvals) mean(fvals)
mc_variance <- function(fvals) mean((fvals - mean(fvals))^2)
mc_standard_error <- function(fvals) sqrt(mc_variance(fvals) / length(fvals))
main <- function() {
  f <- c(2, 4, 4, 4, 5, 5, 7, 9)
  cat("mc_estimate       :", mc_estimate(f), "\n")
  cat("mc_variance       :", mc_variance(f), "\n")
  cat("mc_standard_error :", mc_standard_error(f), "\n")
}
main()
