# Chapter 8 exercise -- one step of backpropagation (Research tier)
# level: research
# HOMEWORK: ch08_text.tex Section 3.  Rscript exercise10.R
# Vectors are numeric vectors; grad_W returns a matrix (rows = classes).

relu_grad <- function(zs) {
  # TODO: element-wise ReLU derivative, 1 where z > 0 else 0
  stop("TODO: relu_grad")
}
grad_logits <- function(p, y) {
  # TODO: delta at the logits of a softmax+CE head, p - y
  stop("TODO: grad_logits")
}
grad_W <- function(delta, x) {
  # TODO: outer product delta %o% x  ->  matrix with [i, j] = delta[i] * x[j]
  stop("TODO: grad_W")
}

main <- function() {
  cat("relu_grad  :", relu_grad(c(-1, 0, 2)), "\n")
  p <- c(0.7, 0.2, 0.1); y <- c(1, 0, 0)
  delta <- grad_logits(p, y)
  cat("grad_logits:", delta, "\n")
  cat("grad_W     :\n"); print(grad_W(delta, c(1, 2)))
}
main()
