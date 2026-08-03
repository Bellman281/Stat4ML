# Chapter 1 exercise 2 -- K-means clustering (distance, assignment, and update)
# Part II: Introduction to Statistical Learning
#
# HOMEWORK: implement each TODO. This fleshes out "Unsupervised
# Learning" (ch01_text.tex Section 2) into a full Lloyd's-algorithm
# iteration: assign points to their nearest centroid, then recompute
# each centroid as the mean of its assigned points.
#
# Run with:  Rscript exercise02.R
# Reference solution: solutions/exercise02_solution.R

euclidean_dist2 <- function(p, q) {
  # TODO: squared Euclidean distance between 2D points p=c(x,y), q=c(x,y).
  stop("TODO: euclidean_dist2")
}

kmeans_assign <- function(points, centroids) {
  # TODO: `points` and `centroids` are lists of c(x,y) vectors. Return
  # a vector of nearest-centroid indices (1-based) for each point.
  stop("TODO: kmeans_assign")
}

kmeans_update_centroids <- function(points, assignments, k) {
  # TODO: recompute each of the k centroids as the mean of the points
  # currently assigned to it. Return a list of k c(x,y) vectors.
  stop("TODO: kmeans_update_centroids")
}

kmeans_iterate <- function(points, centroids, n_iters) {
  # Provided for you -- not part of this exercise.
  for (iter in 1:n_iters) {
    assignments <- kmeans_assign(points, centroids)
    centroids <- kmeans_update_centroids(points, assignments, length(centroids))
  }
  centroids
}

main <- function() {
  cat(sprintf("euclidean_dist2((0,0),(3,4)) = %g  (expect 25)\n", euclidean_dist2(c(0, 0), c(3, 4))))

  points <- list(c(0.0, 0.0), c(0.2, 0.1), c(5.0, 5.0), c(5.1, 4.9))
  centroids <- list(c(1.0, 1.0), c(4.0, 4.0))
  assignments <- kmeans_assign(points, centroids)
  cat("assignments ="); print(assignments); cat("(expect 1 1 2 2)\n")

  updated <- kmeans_update_centroids(points, assignments, 2)
  cat("updated centroids =\n"); print(updated)

  final <- kmeans_iterate(points, centroids, 5)
  cat("after 5 iterations =\n"); print(final)
}

main()
