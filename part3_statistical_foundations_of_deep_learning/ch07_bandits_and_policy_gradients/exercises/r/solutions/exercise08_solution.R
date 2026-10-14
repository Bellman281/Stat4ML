# Chapter 7 -- reference solution (Proof, R)
# level: proof
softmax <- function(logits) { e <- exp(logits - max(logits)); e / sum(e) }
logit_score <- function(a, probs) {
  ind <- rep(0, length(probs)); ind[a] <- 1
  ind - probs
}
pg_grad <- function(R, a, probs) R * logit_score(a, probs)
main <- function() {
  p <- softmax(c(0.0, 0.5, -0.5))
  cat("softmax     :", p, "\n")
  cat("logit_score :", logit_score(2, c(0.2, 0.5, 0.3)), "\n")
  cat("pg_grad     :", pg_grad(2.0, 2, c(0.2, 0.5, 0.3)), "\n")
  mean <- rowSums(sapply(seq_along(p), function(a) p[a] * logit_score(a, p)))
  cat("mean score  :", round(mean, 12), "\n")
}
main()
