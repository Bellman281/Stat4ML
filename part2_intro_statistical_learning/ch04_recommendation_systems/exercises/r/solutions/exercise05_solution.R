# Chapter 4 -- reference solution (Proof, R): the ALS ridge update, k = 2
# level: proof
solve2 <- function(M, v) {
  a <- M[1, 1]; b <- M[1, 2]; c <- M[2, 1]; d <- M[2, 2]
  det <- a * d - b * c
  c((d * v[1] - b * v[2]) / det, (-c * v[1] + a * v[2]) / det)
}
predict_rating <- function(q, p) q[1] * p[1] + q[2] * p[2]

ridge_solution_2d <- function(Q, r, lam) {
  a <- 0; b <- 0; d <- 0; g0 <- 0; g1 <- 0
  for (i in seq_len(nrow(Q))) {
    q <- Q[i, ]; ri <- r[i]
    a <- a + q[1] * q[1]; b <- b + q[1] * q[2]; d <- d + q[2] * q[2]
    g0 <- g0 + q[1] * ri; g1 <- g1 + q[2] * ri
  }
  M <- matrix(c(a + lam, b, b, d + lam), 2, 2, byrow = TRUE)  # Q^T Q + lam I
  solve2(M, c(g0, g1))
}

objective <- function(Q, r, p, lam) {
  s <- 0
  for (i in seq_len(nrow(Q))) s <- s + (r[i] - predict_rating(Q[i, ], p))^2
  s + lam * (p[1]^2 + p[2]^2)
}

grad_at <- function(Q, r, p, lam) {
  g0 <- 0; g1 <- 0
  for (i in seq_len(nrow(Q))) {
    q <- Q[i, ]; e <- r[i] - predict_rating(q, p)
    g0 <- g0 - 2 * q[1] * e; g1 <- g1 - 2 * q[2] * e
  }
  c(g0 + 2 * lam * p[1], g1 + 2 * lam * p[2])
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
