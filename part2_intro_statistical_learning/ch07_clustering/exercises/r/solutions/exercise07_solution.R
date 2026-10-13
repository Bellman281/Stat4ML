# Chapter 7 -- reference solution (Core, R)
# level: core
sq_dist <- function(a, b) sum((a - b)^2)
nearest <- function(point, centroids) which.min(sapply(centroids, function(c) sq_dist(point, c)))
centroid <- function(points) {
  n <- length(points)
  c(sum(sapply(points, function(p) p[1])) / n,
    sum(sapply(points, function(p) p[2])) / n)
}
main <- function() {
  cs <- list(c(0, 0), c(5, 5))
  cat("sq_dist :", sq_dist(c(0, 0), c(3, 4)), "\n")
  cat("nearest :", nearest(c(4, 4), cs), "\n")
  cat("centroid:", centroid(list(c(0, 0), c(2, 0), c(1, 6))), "\n")
}
main()
