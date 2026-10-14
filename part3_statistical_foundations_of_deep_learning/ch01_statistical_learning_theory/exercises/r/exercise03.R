# Chapter 1 exercise -- VC capacity (Research tier)
# level: research
# HOMEWORK: ch01_text.tex Section 3.  Rscript exercise03.R
# patterns is a list of 0/1 vectors of length n (observed label patterns).

sauer_bound <- function(n, d) {
  # TODO: sum of choose(n, i) for i = 0..d
  stop("TODO: sauer_bound")
}
vc_bound_term <- function(d, n, delta) {
  # TODO: sqrt((d*(log(2n/d)+1) + log(4/delta)) / n)
  stop("TODO: vc_bound_term")
}
shatters <- function(patterns, n) {
  # TODO: TRUE iff the DISTINCT patterns number 2^n
  stop("TODO: shatters")
}

main <- function() {
  cat("sauer_bound(5,2) :", sauer_bound(5, 2), "\n")
  cat("vc_bound_term    :", vc_bound_term(10, 1000, 0.05), "\n")
  full <- list(c(0, 0), c(0, 1), c(1, 0), c(1, 1))
  cat("shatters(full,2) :", shatters(full, 2), "\n")
  cat("shatters(part,2) :", shatters(list(c(0, 0), c(1, 1)), 2), "\n")
}
main()
