# Chapter 5 exercise -- Variance and covariance (Core)
# level: core
# HOMEWORK: ch05_text.tex Section 1.  Rscript exercise05.R

center <- function(v) {
  # TODO: v - mean(v)
  stop("TODO: center")
}
variance <- function(v) {
  # TODO: mean((v - mean(v))^2)
  stop("TODO: variance")
}
covariance <- function(x, y) {
  # TODO: mean((x - mean(x)) * (y - mean(y)))
  stop("TODO: covariance")
}
variance_explained_ratio <- function(eigvals) {
  # TODO: eigvals / sum(eigvals)
  stop("TODO: variance_explained_ratio")
}

main <- function() {
  cat("center      :", center(c(1, 2, 3)), "\n")
  cat("variance    :", variance(c(1, 2, 3)), "\n")
  cat("covariance  :", covariance(c(1, 2, 3), c(1, 2, 3)), "\n")
  cat("var ratio   :", variance_explained_ratio(c(3, 1)), "\n")
}
main()
