# Chapter 5 -- reference solution (Research, R)
# level: research
cumulative_variance_explained <- function(eigvals) cumsum(eigvals) / sum(eigvals)
reconstruction_error_ratio <- function(eigvals, k) sum(eigvals[(k+1):length(eigvals)]) / sum(eigvals)
singular_value_from_eigenvalue <- function(eigval) sqrt(eigval)
main <- function() {
  cat("cumulative    :", cumulative_variance_explained(c(4, 1)), "\n")
  cat("recon error   :", reconstruction_error_ratio(c(4, 1), 1), "\n")
  cat("singular value:", singular_value_from_eigenvalue(9), "\n")
}
main()
