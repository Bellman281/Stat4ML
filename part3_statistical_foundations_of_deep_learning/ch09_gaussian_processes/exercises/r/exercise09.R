# Chapter 9 exercise -- kernels (Core tier)
# level: core
# HOMEWORK: ch09_text.tex Section 1.  Rscript exercise09.R

rbf_kernel <- function(x1, x2, length) {
  # TODO: exp(-(x1 - x2)^2 / (2 * length^2))
  stop("TODO: rbf_kernel")
}
kernel_vector <- function(x, xs, length) {
  # TODO: rbf_kernel(x, xi, length) for each xi in xs
  stop("TODO: kernel_vector")
}
linear_kernel <- function(x1, x2) {
  # TODO: x1 * x2
  stop("TODO: linear_kernel")
}

main <- function() {
  cat("rbf_kernel(0,0) :", rbf_kernel(0.0, 0.0, 1.0), "\n")
  cat("rbf_kernel(0,1) :", rbf_kernel(0.0, 1.0, 1.0), "\n")
  cat("kernel_vector   :", kernel_vector(0.0, c(0.0, 1.0, 2.0), 1.0), "\n")
  cat("linear_kernel   :", linear_kernel(2.0, 3.0), "\n")
}
main()
