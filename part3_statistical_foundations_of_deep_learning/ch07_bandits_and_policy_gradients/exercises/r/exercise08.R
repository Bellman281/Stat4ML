# Chapter 7 exercise -- the policy gradient and the score (Proof tier)
# level: proof
# HOMEWORK: ch07_text.tex Section 2.  Rscript exercise08.R
# Softmax policy; score of action a (1-based) is the vector e_a - p.

softmax <- function(logits) { e <- exp(logits - max(logits)); e / sum(e) }

logit_score <- function(a, probs) {
  # TODO: for each i, (1 if i==a else 0) - probs[i].  Hint: diag-like indicator.
  stop("TODO: logit_score")
}
pg_grad <- function(R, a, probs) {
  # TODO: R * logit_score(a, probs)
  stop("TODO: pg_grad")
}

main <- function() {
  p <- softmax(c(0.0, 0.5, -0.5))
  cat("softmax     :", p, "\n")
  cat("logit_score :", logit_score(2, c(0.2, 0.5, 0.3)), "\n")
  cat("pg_grad     :", pg_grad(2.0, 2, c(0.2, 0.5, 0.3)), "\n")
  mean <- rowSums(sapply(seq_along(p), function(a) p[a] * logit_score(a, p)))
  cat("mean score  :", round(mean, 12), "\n")
}
main()
