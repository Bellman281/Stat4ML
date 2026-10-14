# Chapter 9 -- reference solution (Core, R)
# level: core
rbf_kernel <- function(x1, x2, length) exp(-(x1 - x2)^2 / (2 * length^2))
kernel_vector <- function(x, xs, length) sapply(xs, function(xi) rbf_kernel(x, xi, length))
linear_kernel <- function(x1, x2) x1 * x2
main <- function() {
  cat("rbf_kernel(0,0) :", rbf_kernel(0.0, 0.0, 1.0), "\n")
  cat("rbf_kernel(0,1) :", rbf_kernel(0.0, 1.0, 1.0), "\n")
  cat("kernel_vector   :", kernel_vector(0.0, c(0.0, 1.0, 2.0), 1.0), "\n")
  cat("linear_kernel   :", linear_kernel(2.0, 3.0), "\n")
}
main()
