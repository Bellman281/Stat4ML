# Chapter 8 exercise -- activation functions (Core tier)
# level: core
# HOMEWORK: ch08_text.tex Section 1.  Rscript exercise08.R
# softmax must be the STABLE version: subtract max(zs) before exp().

sigmoid <- function(z) {
  # TODO: 1 / (1 + exp(-z))
  stop("TODO: sigmoid")
}
relu <- function(z) {
  # TODO: max(0, z)
  stop("TODO: relu")
}
softmax <- function(zs) {
  # TODO: stable softmax -> probabilities summing to 1 (subtract max(zs) first)
  stop("TODO: softmax")
}

main <- function() {
  cat("sigmoid(0) :", sigmoid(0), "\n")
  cat("relu(-2,3) :", relu(-2), relu(3), "\n")
  cat("softmax    :", softmax(c(1, 1, 1)), "\n")
  cat("softmax big:", softmax(c(1000, 1000)), "\n")
}
main()
