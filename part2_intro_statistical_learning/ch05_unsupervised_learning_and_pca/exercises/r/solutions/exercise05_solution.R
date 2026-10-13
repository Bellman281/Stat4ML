# Chapter 5 -- reference solution (Core, R)
# level: core
center <- function(v) v - mean(v)
variance <- function(v) mean((v - mean(v))^2)
covariance <- function(x, y) mean((x - mean(x)) * (y - mean(y)))
variance_explained_ratio <- function(eigvals) eigvals / sum(eigvals)
main <- function() {
  cat("center      :", center(c(1, 2, 3)), "\n")
  cat("variance    :", variance(c(1, 2, 3)), "\n")
  cat("covariance  :", covariance(c(1, 2, 3), c(1, 2, 3)), "\n")
  cat("var ratio   :", variance_explained_ratio(c(3, 1)), "\n")
}
main()
