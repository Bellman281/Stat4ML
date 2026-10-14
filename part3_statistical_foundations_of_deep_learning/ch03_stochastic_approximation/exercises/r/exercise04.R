# Chapter 3 exercise -- the Robbins-Monro conditions (Proof tier)
# level: proof
# HOMEWORK: ch03_text.tex Section 2.  Rscript exercise04.R
# a_t = 1/t^p is a VALID schedule iff 1/2 < p <= 1.

harmonic_partial <- function(T) {
  # TODO: sum of 1/t for t = 1..T
  stop("TODO: harmonic_partial")
}
basel_partial <- function(T) {
  # TODO: sum of 1/t^2 for t = 1..T
  stop("TODO: basel_partial")
}
rm_valid <- function(p) {
  # TODO: TRUE iff 1/2 < p <= 1
  stop("TODO: rm_valid")
}

main <- function() {
  cat("harmonic_partial(4):", harmonic_partial(4), "\n")
  cat("basel_partial(1000) :", basel_partial(1000), " (pi^2/6 = 1.6449..)\n")
  for (p in c(1.0, 0.75, 0.5, 0.4)) cat(sprintf("rm_valid(%.2f) : %s\n", p, rm_valid(p)))
}
main()
