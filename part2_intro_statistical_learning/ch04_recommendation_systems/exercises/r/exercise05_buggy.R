# Chapter 4 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# The ALS update is the ridge estimator p = (Q^T Q + lam I)^{-1} Q^T r
# (Theorem 2.1). Two deliberate bugs (ridge_solution_2d, grad_at).
# Do not edit run_tests().

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
  # BUG: the ridge term lam*I is missing from the diagonal, so this solves the
  # UNREGULARIZED normal equations -- not a stationary point of the penalised
  # objective (Theorem 2.1), and singular when a user rated fewer than k items.
  M <- matrix(c(a, b, b, d), 2, 2, byrow = TRUE)
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
    # BUG: data-term gradient of (r - q.p)^2 is -2 (r - q.p) q; sign flipped.
    g0 <- g0 + 2 * q[1] * e; g1 <- g1 + 2 * q[2] * e
  }
  c(g0 + 2 * lam * p[1], g1 + 2 * lam * p[2])
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  Q <- matrix(c(2, 0, 0, 1), 2, 2, byrow = TRUE)
  r <- c(4, 3); lam <- 1
  p <- ridge_solution_2d(Q, r, lam)
  check("ridge_p0", p[1], 1.6)
  check("ridge_p1", p[2], 1.5)
  check("objective", objective(Q, r, c(1.6, 1.5), lam), 7.7)
  g <- grad_at(Q, r, c(1, 1), lam)
  check("grad0", g[1], -6.0)
  check("grad1", g[2], -2.0)
  gstar <- grad_at(Q, r, p, lam)
  check("optimality_0", gstar[1], 0.0, tol = 1e-6)
  check("optimality_1", gstar[2], 0.0, tol = 1e-6)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
