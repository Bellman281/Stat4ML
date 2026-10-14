# Chapter 3 exercise -- the SGD step and schedules (Core tier)
# level: core
# HOMEWORK: ch03_text.tex Sections 1-2.  Rscript exercise03.R

sgd_step <- function(theta, grad, lr) {
  # TODO: theta - lr * grad
  stop("TODO: sgd_step")
}
inverse_time_lr <- function(t, a0) {
  # TODO: a0 / t
  stop("TODO: inverse_time_lr")
}
quad_grad <- function(theta, target) {
  # TODO: 2 * (theta - target)
  stop("TODO: quad_grad")
}

main <- function() {
  cat("sgd_step        :", sgd_step(5.0, 2.0, 0.1), "\n")
  cat("inverse_time_lr :", inverse_time_lr(4, 0.5), "\n")
  cat("quad_grad       :", quad_grad(5.0, 3.0), "\n")
  cat("one step toward 3:", sgd_step(5.0, quad_grad(5.0, 3.0), 0.25), "\n")
}
main()
