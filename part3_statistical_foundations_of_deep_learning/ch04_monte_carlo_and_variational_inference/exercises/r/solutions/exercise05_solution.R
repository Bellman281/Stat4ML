# Chapter 4 -- reference solution (Proof, R)
# level: proof
importance_weight <- function(px, qx) px / qx
is_estimate <- function(fvals, pxs, qxs) mean(fvals * pxs / qxs)
eff_sample_size <- function(weights) sum(weights)^2 / sum(weights^2)
main <- function() {
  cat("importance_weight :", importance_weight(0.1, 0.2), "\n")
  cat("is_estimate       :", is_estimate(c(1, 1), c(0.2, 0.2), c(0.4, 0.4)), "\n")
  cat("eff_sample_size u :", eff_sample_size(c(1, 1, 1, 1)), "\n")
  cat("eff_sample_size s :", eff_sample_size(c(2, 0, 0, 0)), "\n")
}
main()
