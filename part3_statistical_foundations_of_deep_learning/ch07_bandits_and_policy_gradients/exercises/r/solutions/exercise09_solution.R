# Chapter 7 -- reference solution (Research, R)
# level: research
logit_score <- function(a, probs) {
  ind <- rep(0, length(probs)); ind[a] <- 1
  ind - probs
}
advantage <- function(R, baseline) R - baseline
grad_estimate <- function(R, b, a, probs) (R - b) * logit_score(a, probs)
expected_grad <- function(rewards, b, probs) {
  acc <- rep(0, length(probs))
  for (a in seq_along(probs)) acc <- acc + probs[a] * grad_estimate(rewards[a], b, a, probs)
  acc
}
main <- function() {
  probs <- c(0.2, 0.5, 0.3); rewards <- c(1.0, 2.0, 3.0)
  cat("advantage       :", advantage(3.0, 2.0), "\n")
  cat("grad_estimate   :", grad_estimate(3.0, 2.0, 2, probs), "\n")
  cat("E[grad], b=0    :", round(expected_grad(rewards, 0.0, probs), 6), "\n")
  cat("E[grad], b=5    :", round(expected_grad(rewards, 5.0, probs), 6), "\n")
}
main()
