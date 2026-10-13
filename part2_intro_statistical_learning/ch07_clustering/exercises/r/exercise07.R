# Chapter 7 exercise -- k-means primitives (Core tier)
# level: core
# HOMEWORK: ch07_text.tex Sections 1-2.  Rscript exercise07.R
# A 2D point is a numeric vector c(x, y); a set of points is a list of them.

sq_dist <- function(a, b) {
  # TODO: squared Euclidean distance sum((a - b)^2)
  stop("TODO: sq_dist")
}
nearest <- function(point, centroids) {
  # TODO: index (1-based) of the centroid closest to point; use which.min
  stop("TODO: nearest")
}
centroid <- function(points) {
  # TODO: mean point c(mean_x, mean_y)
  stop("TODO: centroid")
}

main <- function() {
  cs <- list(c(0, 0), c(5, 5))
  cat("sq_dist :", sq_dist(c(0, 0), c(3, 4)), "\n")
  cat("nearest :", nearest(c(4, 4), cs), "\n")
  cat("centroid:", centroid(list(c(0, 0), c(2, 0), c(1, 6))), "\n")
}
main()
