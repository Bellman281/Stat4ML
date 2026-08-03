# Chapter 0 -- RUSTLINGS-STYLE EXERCISE (R edition), Exercise 2
# Part I: Statistics Foundation for ML
#
# Two deliberate bugs are hiding in lu_decompose_2x2 (wrong pivot for
# l21, and a u22 that forgets to subtract the update term). Run this
# file, read the first failing check, fix ONLY that bug, and re-run --
# repeat until you see "All tests passed!". Do not edit run_tests().
#
# Run with:  Rscript exercise02_buggy.R

matmul <- function(A, B) {
  # Correct.
  n <- nrow(A); k <- ncol(A); m <- ncol(B)
  C <- matrix(0, nrow = n, ncol = m)
  for (i in 1:n) for (j in 1:m) {
    s <- 0
    for (t in 1:k) s <- s + A[i, t] * B[t, j]
    C[i, j] <- s
  }
  C
}

lu_decompose_2x2 <- function(A) {
  a11 <- A[1, 1]; a12 <- A[1, 2]; a21 <- A[2, 1]; a22 <- A[2, 2]
  u11 <- a11; u12 <- a12
  # BUG: divides by a22 (wrong pivot) instead of a11 -- see
  # ch00_text.tex Section 6.1, l21 = a21 / a11.
  l21 <- a21 / a22
  # BUG: forgets to subtract l21 * u12 -- returns a22 unchanged instead
  # of the Schur-complement update u22 = a22 - l21 * u12.
  u22 <- a22
  L <- matrix(c(1, 0, l21, 1), nrow = 2, byrow = TRUE)
  U <- matrix(c(u11, u12, 0, u22), nrow = 2, byrow = TRUE)
  list(L = L, U = U)
}

reconstruct <- function(L, U) {
  # Correct.
  matmul(L, U)
}

# ---------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# ---------------------------------------------------------------------------
run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- all(abs(got - expected) < tol)
    status <- if (ok) "PASS" else "FAIL"
    cat(sprintf("[%s] %s\n", status, name))
    if (!ok) failures <<- c(failures, name)
  }

  A <- matrix(c(4, 3, 6, 3), nrow = 2, byrow = TRUE)
  lu <- lu_decompose_2x2(A)
  check("L", lu$L, matrix(c(1, 0, 1.5, 1), nrow = 2, byrow = TRUE))
  check("U", lu$U, matrix(c(4, 3, 0, -1.5), nrow = 2, byrow = TRUE))
  check("reconstruct(L, U) == A", reconstruct(lu$L, lu$U), A)

  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED: %s\n", length(failures), paste(failures, collapse = ", ")))
    quit(status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
