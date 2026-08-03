# Reference solution for exercise02.R (Chapter 1, Part II, Exercise 2)

euclidean_dist2 <- function(p, q) {
  (p[1] - q[1])^2 + (p[2] - q[2])^2
}

kmeans_assign <- function(points, centroids) {
  sapply(points, function(p) {
    dists <- sapply(centroids, function(c) euclidean_dist2(p, c))
    which.min(dists)
  })
}

kmeans_update_centroids <- function(points, assignments, k) {
  result <- vector("list", k)
  for (i in 1:k) {
    assigned <- points[assignments == i]
    xs <- sapply(assigned, function(p) p[1])
    ys <- sapply(assigned, function(p) p[2])
    result[[i]] <- c(mean(xs), mean(ys))
  }
  result
}

kmeans_iterate <- function(points, centroids, n_iters) {
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
