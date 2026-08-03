# Chapter 0 -- RUSTLINGS-STYLE EXERCISE (R edition), Exercise 1
# Part I: Statistics Foundation for ML
#
# Three deliberate bugs are hiding below (in transpose, det2x2, and
# inverse2x2). Run this file, read the first failing check, fix ONLY
# that function, and re-run -- repeat until you see "All tests
# passed!". Do not edit run_tests().
#
# Run with:  Rscript exercise01_buggy.R

matmul <- function(A, B) {
  # Correct.
  n <- nrow(A); k <- ncol(A); m <- ncol(B)
  C <- matrix(0, nrow = n, ncol = m)
  for (i in 1:n) {
    for (j in 1:m) {
      s <- 0
      for (t in 1:k) s <- s + A[i, t] * B[t, j]
      C[i, j] <- s
    }
  }
  C
}

transpose <- function(A) {
  # BUG: returns A unchanged -- forgets to swap row/column indices
  # (see ch00_text.tex Definition 4.1).
  A
}

det2x2 <- function(A) {
  # BUG: computes a*d + b*c instead of a*d - b*c (sign error -- see
  # ch00_text.tex Section 2).
  A[1, 1] * A[2, 2] + A[1, 2] * A[2, 1]
}

inverse2x2 <- function(A) {
  # BUG: forgets to divide by det(A) -- returns just the adjugate
  # matrix [[d,-b],[-c,a]] (see ch00_text.tex Section 3).
  matrix(c(A[2, 2], -A[1, 2], -A[2, 1], A[1, 1]), nrow = 2, byrow = TRUE)
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

  A <- matrix(c(1, 2, 3, 4), nrow = 2, byrow = TRUE)
  B <- matrix(c(5, 6, 7, 8), nrow = 2, byrow = TRUE)
  AB <- matmul(A, B)
  check("matmul(A,B)", AB, matrix(c(19, 22, 43, 50), nrow = 2, byrow = TRUE))

  lhs <- transpose(AB)
  rhs <- matmul(transpose(B), transpose(A))
  check("(AB)^T == B^T A^T", lhs, rhs)

  dA <- det2x2(A); dB <- det2x2(B); dAB <- det2x2(AB)
  check("det(A)*det(B) == det(AB)", dA * dB, dAB)

  invA <- inverse2x2(A)
  check_mat <- matmul(A, invA)
  check("A @ inverse(A) == I", check_mat, diag(2))

  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED: %s\n", length(failures), paste(failures, collapse = ", ")))
    quit(status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
