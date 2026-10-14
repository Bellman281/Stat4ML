# Chapter 4 exercise -- the ALS ridge update (Proof tier, R)
# level: proof
# HOMEWORK: ch04_text.tex Section 2 / Theorem 2.1.
# p = (Q^T Q + lam I)^{-1} Q^T r.  k = 2, so solve2() (given) does the 2x2 solve.

solve2 <- function(M, v) {
  a <- M[1, 1]; b <- M[1, 2]; c <- M[2, 1]; d <- M[2, 2]
  det <- a * d - b * c
  c((d * v[1] - b * v[2]) / det, (-c * v[1] + a * v[2]) / det)
}
predict_rating <- function(q, p) q[1] * p[1] + q[2] * p[2]

ridge_solution_2d <- function(Q, r, lam) {
  # TODO: accumulate Q^T Q (2x2) and Q^T r (length 2), add lam to the diagonal,
  # then return solve2(Q^T Q + lam I, Q^T r). Rows of Q are the rated items.
  stop("TODO: ridge_solution_2d")
}
objective <- function(Q, r, p, lam) {
  # TODO: sum_i (r_i - q_i.p)^2 + lam * |p|^2
  stop("TODO: objective")
}
grad_at <- function(Q, r, p, lam) {
  # TODO: -2 Q^T (r - Q p) + 2 lam p, returned as a length-2 vector
  stop("TODO: grad_at")
}

main <- function() {
  Q <- matrix(c(2, 0, 0, 1), 2, 2, byrow = TRUE)
  r <- c(4, 3); lam <- 1
  p <- ridge_solution_2d(Q, r, lam)
  cat("ALS solution p :", p, "\n")
  cat("objective      :", objective(Q, r, p, lam), "\n")
  cat("grad at p      :", grad_at(Q, r, p, lam), "\n")
}
main()
