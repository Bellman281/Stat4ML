# Chapter 1 -- RUSTLINGS-STYLE EXERCISE (R edition), Exercise 2
# Part II: Introduction to Statistical Learning
#
# Three deliberate bugs are hiding below (in euclidean_dist2,
# kmeans_assign, and kmeans_update_centroids). Run this file, read the
# first failing check, fix ONLY that function, and re-run -- repeat
# until you see "All tests passed!". Do not edit run_tests().
#
# Run with:  Rscript exercise02_buggy.R

euclidean_dist2 <- function(p, q) {
  # BUG: subtracts instead of adds the two squared terms.
  (p[1] - q[1])^2 - (p[2] - q[2])^2
}

kmeans_assign <- function(points, centroids) {
  # BUG: uses which.max instead of which.min -- assigns to the FARTHEST
  # centroid instead of the nearest.
  sapply(points, function(p) {
    dists <- sapply(centroids, function(c) euclidean_dist2(p, c))
    which.max(dists)
  })
}

kmeans_update_centroids <- function(points, assignments, k) {
  # BUG: ignores `assignments` -- every centroid becomes the mean of
  # ALL points.
  xs <- sapply(points, function(p) p[1])
  ys <- sapply(points, function(p) p[2])
  result <- vector("list", k)
  for (i in 1:k) result[[i]] <- c(mean(xs), mean(ys))
  result
}

kmeans_iterate <- function(points, centroids, n_iters) {
  # Correct.
  for (iter in 1:n_iters) {
    assignments <- kmeans_assign(points, centroids)
    centroids <- kmeans_update_centroids(points, assignments, length(centroids))
  }
  centroids
}

# ---------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# ---------------------------------------------------------------------------
run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- all(abs(unlist(got) - unlist(expected)) < tol)
    status <- if (ok) "PASS" else "FAIL"
    cat(sprintf("[%s] %s\n", status, name))
    if (!ok) failures <<- c(failures, name)
  }

  check("euclidean_dist2((0,0),(3,4))", euclidean_dist2(c(0, 0), c(3, 4)), 25)

  points <- list(c(0.0, 0.0), c(0.2, 0.1), c(5.0, 5.0), c(5.1, 4.9))
  centroids <- list(c(1.0, 1.0), c(4.0, 4.0))
  assignments <- kmeans_assign(points, centroids)
  check("kmeans_assign", assignments, c(1, 1, 2, 2))

  updated <- kmeans_update_centroids(points, c(1, 1, 2, 2), 2)
  check("kmeans_update_centroids", updated, list(c(0.1, 0.05), c(5.05, 4.95)))

  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED: %s\n", length(failures), paste(failures, collapse = ", ")))
    quit(status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
