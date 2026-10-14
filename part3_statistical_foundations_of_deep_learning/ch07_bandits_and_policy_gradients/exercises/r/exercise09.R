# Chapter 7 exercise -- baselines as control variates (Research tier)
# level: research
# HOMEWORK: ch07_text.tex Section 3.  Rscript exercise09.R

logit_score <- function(a, probs) {       # provided (from Section 2)
  ind <- rep(0, length(probs)); ind[a] <- 1
  ind - probs
}

advantage <- function(R, baseline) {
  # TODO: R - baseline
  stop("TODO: advantage")
}
grad_estimate <- function(R, b, a, probs) {
  # TODO: (R - b) * logit_score(a, probs)
  stop("TODO: grad_estimate")
}
expected_grad <- function(rewards, b, probs) {
  # TODO: sum_a probs[a] * grad_estimate(rewards[a], b, a, probs)
  stop("TODO: expected_grad")
}

main <- function() {
  probs <- c(0.2, 0.5, 0.3); rewards <- c(1.0, 2.0, 3.0)
  cat("advantage       :", advantage(3.0, 2.0), "\n")
  cat("grad_estimate   :", grad_estimate(3.0, 2.0, 2, probs), "\n")
  cat("E[grad], b=0    :", round(expected_grad(rewards, 0.0, probs), 6), "\n")
  cat("E[grad], b=5    :", round(expected_grad(rewards, 5.0, probs), 6), "\n")
}
main()
