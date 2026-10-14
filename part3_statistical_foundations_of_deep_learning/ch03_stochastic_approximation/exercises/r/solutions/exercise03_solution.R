# Chapter 3 -- reference solution (Core, R)
# level: core
sgd_step <- function(theta, grad, lr) theta - lr * grad
inverse_time_lr <- function(t, a0) a0 / t
quad_grad <- function(theta, target) 2 * (theta - target)
main <- function() {
  cat("sgd_step        :", sgd_step(5.0, 2.0, 0.1), "\n")
  cat("inverse_time_lr :", inverse_time_lr(4, 0.5), "\n")
  cat("quad_grad       :", quad_grad(5.0, 3.0), "\n")
  cat("one step toward 3:", sgd_step(5.0, quad_grad(5.0, 3.0), 0.25), "\n")
}
main()
