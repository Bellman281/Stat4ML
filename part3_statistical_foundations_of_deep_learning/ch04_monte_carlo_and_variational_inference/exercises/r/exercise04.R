# Chapter 4 exercise -- Monte Carlo estimation (Core tier)
# level: core
# HOMEWORK: ch04_text.tex Section 1.  Rscript exercise04.R

mc_estimate <- function(fvals) {
  # TODO: mean(fvals)
  stop("TODO: mc_estimate")
}
mc_variance <- function(fvals) {
  # TODO: population variance, mean((fvals - mean(fvals))^2)
  stop("TODO: mc_variance")
}
mc_standard_error <- function(fvals) {
  # TODO: sqrt(mc_variance(fvals) / length(fvals))
  stop("TODO: mc_standard_error")
}

main <- function() {
  f <- c(2, 4, 4, 4, 5, 5, 7, 9)
  cat("mc_estimate       :", mc_estimate(f), "\n")
  cat("mc_variance       :", mc_variance(f), "\n")
  cat("mc_standard_error :", mc_standard_error(f), "\n")
}
main()
