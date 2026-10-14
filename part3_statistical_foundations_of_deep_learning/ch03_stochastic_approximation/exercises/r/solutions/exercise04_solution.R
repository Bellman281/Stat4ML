# Chapter 3 -- reference solution (Proof, R)
# level: proof
harmonic_partial <- function(T) sum(1 / seq_len(T))
basel_partial <- function(T) sum(1 / seq_len(T)^2)
rm_valid <- function(p) (p > 0.5) && (p <= 1.0)
main <- function() {
  cat("harmonic_partial(4):", harmonic_partial(4), "\n")
  cat("basel_partial(1000) :", basel_partial(1000), " (pi^2/6 = 1.6449..)\n")
  for (p in c(1.0, 0.75, 0.5, 0.4)) cat(sprintf("rm_valid(%.2f) : %s\n", p, rm_valid(p)))
}
main()
