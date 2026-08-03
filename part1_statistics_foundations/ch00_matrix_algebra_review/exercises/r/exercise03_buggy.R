# Chapter 0 -- RUSTLINGS-STYLE EXERCISE (R edition), Exercise 3
# Part I: Statistics Foundation for ML
#
# Two deliberate bugs are hiding below (in trace_, and in the
# discriminant inside eigenvalues_2x2). Run this file, read the first
# failing check, fix ONLY that bug, and re-run -- repeat until you see
# "All tests passed!". Do not edit run_tests().
#
# Run with:  Rscript exercise03_buggy.R

trace_ <- function(A) {
  # BUG: sums all four entries of A instead of just the two diagonal
  # entries (see ch00_text.tex Section 5, trace(A) = a11 + a22).
  A[1, 1] + A[1, 2] + A[2, 1] + A[2, 2]
}

det2x2 <- function(A) {
  # Correct.
  A[1, 1] * A[2, 2] - A[1, 2] * A[2, 1]
}

eigenvalues_2x2 <- function(A) {
  tr <- trace_(A)
  d <- det2x2(A)
  # BUG: discriminant should be trace(A)^2 - 4*det(A), not
  # trace(A)^2 - det(A) -- see ch00_text.tex Section 5, Theorem 5.1.
  disc <- sqrt(tr * tr - d)
  c((tr + disc) / 2, (tr - disc) / 2)
}

eigenvector_for_eigenvalue_2x2 <- function(A, lam) {
  # Correct (not part of this exercise).
  a <- A[1, 1]; b <- A[1, 2]; c <- A[2, 1]; d <- A[2, 2]
  if (abs(b) > 1e-12) {
    v <- c(b, lam - a)
  } else {
    v <- c(lam - d, c)
  }
  v / sqrt(sum(v^2))
}

# ---------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# ---------------------------------------------------------------------------
run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- all(abs(got - expected) < tol)
    status <- if (ok) "PASS" else "FAIL"
    cat(sprintf("[%s] %s: got=%s expected=%s\n", status, name,
                 paste(got, collapse=","), paste(expected, collapse=",")))
    if (!ok) failures <<- c(failures, name)
  }

  A <- matrix(c(0.8, 0.3, 0.2, 0.7), nrow = 2, byrow = TRUE)
  check("trace_(A)", trace_(A), 1.5)

  lams <- eigenvalues_2x2(A)
  check("eigenvalues sum to trace(A)", sum(lams), trace_(A))
  check("eigenvalues product equals det(A)", prod(lams), det2x2(A))
  check("lambda1", round(lams[1], 6), 1.0)
  check("lambda2", round(lams[2], 6), 0.5)

  v1 <- eigenvector_for_eigenvalue_2x2(A, lams[1])
  Av1 <- c(A[1, 1] * v1[1] + A[1, 2] * v1[2], A[2, 1] * v1[1] + A[2, 2] * v1[2])
  check("A@v1 == lambda1*v1", Av1, lams[1] * v1)

  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED: %s\n", length(failures), paste(failures, collapse = ", ")))
    quit(status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
