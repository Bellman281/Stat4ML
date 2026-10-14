# Chapter 1 -- reference solution (Research, R)
# level: research
sauer_bound <- function(n, d) sum(choose(n, 0:d))
vc_bound_term <- function(d, n, delta) sqrt((d * (log(2 * n / d) + 1) + log(4 / delta)) / n)
shatters <- function(patterns, n) length(unique(patterns)) == 2^n
main <- function() {
  cat("sauer_bound(5,2) :", sauer_bound(5, 2), "\n")
  cat("vc_bound_term    :", vc_bound_term(10, 1000, 0.05), "\n")
  full <- list(c(0, 0), c(0, 1), c(1, 0), c(1, 1))
  cat("shatters(full,2) :", shatters(full, 2), "\n")
  cat("shatters(part,2) :", shatters(list(c(0, 0), c(1, 1)), 2), "\n")
}
main()
