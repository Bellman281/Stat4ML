# Chapter 5 exercise -- entropy, cross-entropy, KL (Core tier)
# level: core
# HOMEWORK: ch05_text.tex Section 1.  Rscript exercise05.R
# p and q are probability vectors (sum to 1, all > 0). Work in nats.

entropy <- function(p) {
  # TODO: -sum(p * log(p))
  stop("TODO: entropy")
}
cross_entropy <- function(p, q) {
  # TODO: -sum(p * log(q))
  stop("TODO: cross_entropy")
}
kl <- function(p, q) {
  # TODO: sum(p * log(p / q))
  stop("TODO: kl")
}

main <- function() {
  p <- c(0.5, 0.5); q <- c(0.25, 0.75)
  cat("entropy      :", entropy(p), "\n")
  cat("cross_entropy:", cross_entropy(p, q), "\n")
  cat("kl           :", kl(p, q), "\n")
}
main()
