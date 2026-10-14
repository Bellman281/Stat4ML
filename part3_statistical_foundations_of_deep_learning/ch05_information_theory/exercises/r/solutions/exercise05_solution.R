# Chapter 5 -- reference solution (Core, R)
# level: core
entropy <- function(p) -sum(p * log(p))
cross_entropy <- function(p, q) -sum(p * log(q))
kl <- function(p, q) sum(p * log(p / q))
main <- function() {
  p <- c(0.5, 0.5); q <- c(0.25, 0.75)
  cat("entropy      :", entropy(p), "\n")
  cat("cross_entropy:", cross_entropy(p, q), "\n")
  cat("kl           :", kl(p, q), "\n")
}
main()
