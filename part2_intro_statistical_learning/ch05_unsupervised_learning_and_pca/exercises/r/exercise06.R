# Chapter 5 exercise -- Variance maximisation and eigenvectors (Proof tier)
# level: proof
# S is a 2x2 covariance matrix.  Rscript exercise06.R

matvec2 <- function(S, w) {
  # TODO: S %*% w as a length-2 vector
  stop("TODO: matvec2")
}
projected_variance <- function(S, w) {
  # TODO: w . (S w)
  stop("TODO: projected_variance")
}
top_eigenvalue_2x2 <- function(S) {
  # TODO: (tr + sqrt(tr^2 - 4*det)) / 2
  stop("TODO: top_eigenvalue_2x2")
}

main <- function() {
  S <- matrix(c(2, 0.8, 0.8, 0.6), 2, 2, byrow = TRUE)
  I <- matrix(c(2, 0, 0, 1), 2, 2, byrow = TRUE)
  cat("matvec2       :", matvec2(I, c(1, 0)), "\n")
  cat("proj variance :", projected_variance(I, c(0.6, 0.8)), "\n")
  cat("top eigenvalue:", top_eigenvalue_2x2(S), "\n")
}
main()
