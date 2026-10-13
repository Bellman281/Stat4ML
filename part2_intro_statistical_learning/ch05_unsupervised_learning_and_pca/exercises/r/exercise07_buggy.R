# Chapter 5 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (reconstruction_error_ratio, singular_value_from_eigenvalue).

cumulative_variance_explained <- function(eigvals) cumsum(eigvals) / sum(eigvals)
reconstruction_error_ratio <- function(eigvals, k) {
  # BUG: the error is the variance DROPPED (after k), not the variance KEPT.
  sum(eigvals[seq_len(k)]) / sum(eigvals)
}
singular_value_from_eigenvalue <- function(eigval) {
  # BUG: a singular value is the SQUARE ROOT of the X^T X eigenvalue.
  eigval
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- length(got) == length(expected) && all(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, paste(format(got), collapse=","), paste(format(expected), collapse=",")))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("cumulative", cumulative_variance_explained(c(4, 1)), c(0.8, 1.0))
  check("recon error", reconstruction_error_ratio(c(4, 1), 1), 0.2)
  check("singular value", singular_value_from_eigenvalue(9), 3.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
