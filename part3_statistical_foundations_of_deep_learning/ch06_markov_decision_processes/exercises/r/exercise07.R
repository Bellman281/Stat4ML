# Chapter 6 exercise -- the Bellman contraction bound (Proof tier)
# level: proof
# HOMEWORK: ch06_text.tex Section 2.  Rscript exercise07.R

sup_norm <- function(v, u) {
  # TODO: max(abs(v - u))
  stop("TODO: sup_norm")
}
geometric_bound <- function(init_err, gamma, k) {
  # TODO: init_err * gamma^k
  stop("TODO: geometric_bound")
}
num_iters_for_tol <- function(init_err, gamma, tol) {
  # TODO: smallest integer k with gamma^k * init_err <= tol (0 if already within tol)
  stop("TODO: num_iters_for_tol")
}

main <- function() {
  cat("sup_norm          :", sup_norm(c(1.0, 2.0, 3.0), c(1.0, 2.0, 5.0)), "\n")
  cat("geometric_bound   :", geometric_bound(10.0, 0.9, 2), "\n")
  cat("num_iters_for_tol :", num_iters_for_tol(1.0, 0.9, 0.01), "\n")
}
main()
