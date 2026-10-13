# Chapter 8 -- reference solution (Core, R)
# level: core
sigmoid <- function(z) 1 / (1 + exp(-z))
relu <- function(z) max(0, z)
softmax <- function(zs) {
  e <- exp(zs - max(zs))
  e / sum(e)
}
main <- function() {
  cat("sigmoid(0) :", sigmoid(0), "\n")
  cat("relu(-2,3) :", relu(-2), relu(3), "\n")
  cat("softmax    :", softmax(c(1, 1, 1)), "\n")
  cat("softmax big:", softmax(c(1000, 1000)), "\n")
}
main()
