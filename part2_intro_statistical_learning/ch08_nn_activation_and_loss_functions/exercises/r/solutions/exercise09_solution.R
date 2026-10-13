# Chapter 8 -- reference solution (Proof, R)
# level: proof
softmax <- function(zs) { e <- exp(zs - max(zs)); e / sum(e) }
cross_entropy <- function(p, y) -sum(y * log(p))
ce_grad <- function(p, y) p - y
main <- function() {
  z <- c(2.0, 0.5, -1.0); y <- c(1, 0, 0); p <- softmax(z)
  cat("p         :", p, "\n")
  cat("loss      :", cross_entropy(p, y), "\n")
  cat("grad (p-y):", ce_grad(p, y), "\n")
}
main()
