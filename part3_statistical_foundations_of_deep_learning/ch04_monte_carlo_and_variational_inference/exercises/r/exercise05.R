# Chapter 4 exercise -- importance sampling (Proof tier)
# level: proof
# HOMEWORK: ch04_text.tex Section 1.  Rscript exercise05.R

importance_weight <- function(px, qx) {
  # TODO: p(x) / q(x)
  stop("TODO: importance_weight")
}
is_estimate <- function(fvals, pxs, qxs) {
  # TODO: mean(fvals * pxs / qxs)
  stop("TODO: is_estimate")
}
eff_sample_size <- function(weights) {
  # TODO: sum(weights)^2 / sum(weights^2)
  stop("TODO: eff_sample_size")
}

main <- function() {
  cat("importance_weight :", importance_weight(0.1, 0.2), "\n")
  cat("is_estimate       :", is_estimate(c(1, 1), c(0.2, 0.2), c(0.4, 0.4)), "\n")
  cat("eff_sample_size u :", eff_sample_size(c(1, 1, 1, 1)), "\n")
  cat("eff_sample_size s :", eff_sample_size(c(2, 0, 0, 0)), "\n")
}
main()
