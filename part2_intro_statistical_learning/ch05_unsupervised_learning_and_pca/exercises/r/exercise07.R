# Chapter 5 exercise -- Singular values and variance explained (Research tier)
# level: research
# HOMEWORK: ch05_text.tex Section 3.  Rscript exercise07.R

cumulative_variance_explained <- function(eigvals) {
  # TODO: cumsum(eigvals) / sum(eigvals)
  stop("TODO: cumulative_variance_explained")
}
reconstruction_error_ratio <- function(eigvals, k) {
  # TODO: sum of the dropped eigenvalues (after k) / total
  stop("TODO: reconstruction_error_ratio")
}
singular_value_from_eigenvalue <- function(eigval) {
  # TODO: sqrt(eigval)
  stop("TODO: singular_value_from_eigenvalue")
}

main <- function() {
  cat("cumulative    :", cumulative_variance_explained(c(4, 1)), "\n")
  cat("recon error   :", reconstruction_error_ratio(c(4, 1), 1), "\n")
  cat("singular value:", singular_value_from_eigenvalue(9), "\n")
}
main()
