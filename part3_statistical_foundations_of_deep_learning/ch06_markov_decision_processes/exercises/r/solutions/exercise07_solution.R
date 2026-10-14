# Chapter 6 -- reference solution (Proof, R)
# level: proof
sup_norm <- function(v, u) max(abs(v - u))
geometric_bound <- function(init_err, gamma, k) init_err * gamma^k
num_iters_for_tol <- function(init_err, gamma, tol) {
  if (init_err <= tol) return(0)
  max(0, ceiling(log(tol / init_err) / log(gamma)))
}
main <- function() {
  cat("sup_norm          :", sup_norm(c(1.0, 2.0, 3.0), c(1.0, 2.0, 5.0)), "\n")
  cat("geometric_bound   :", geometric_bound(10.0, 0.9, 2), "\n")
  cat("num_iters_for_tol :", num_iters_for_tol(1.0, 0.9, 0.01), "\n")
}
main()
