# Chapter 8 -- reference solution (Research, R)
# level: research
relu_grad <- function(zs) as.numeric(zs > 0)
grad_logits <- function(p, y) p - y
grad_W <- function(delta, x) delta %o% x
main <- function() {
  cat("relu_grad  :", relu_grad(c(-1, 0, 2)), "\n")
  p <- c(0.7, 0.2, 0.1); y <- c(1, 0, 0)
  delta <- grad_logits(p, y)
  cat("grad_logits:", delta, "\n")
  cat("grad_W     :\n"); print(grad_W(delta, c(1, 2)))
}
main()
