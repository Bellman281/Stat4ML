# Chapter 8 exercise -- softmax cross-entropy and its gradient (Proof tier)
# level: proof
# HOMEWORK: ch08_text.tex Section 2.  Rscript exercise09.R
# y is a one-hot vector. The test confirms dL/dz = p - y against finite diffs.

softmax <- function(zs) { e <- exp(zs - max(zs)); e / sum(e) }

cross_entropy <- function(p, y) {
  # TODO: L = - sum(y * log(p))
  stop("TODO: cross_entropy")
}
ce_grad <- function(p, y) {
  # TODO: gradient at the logits, p - y
  stop("TODO: ce_grad")
}

main <- function() {
  z <- c(2.0, 0.5, -1.0); y <- c(1, 0, 0); p <- softmax(z)
  cat("p         :", p, "\n")
  cat("loss      :", cross_entropy(p, y), "\n")
  cat("grad (p-y):", ce_grad(p, y), "\n")
}
main()
