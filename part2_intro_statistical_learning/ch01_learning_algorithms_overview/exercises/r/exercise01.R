# Chapter 1 exercise -- Learning Algorithms Overview
# Part II: Introduction to Statistical Learning
#
# HOMEWORK: implement one small example of each of three learning
# paradigms: supervised (closed-form simple linear regression),
# unsupervised (a single K-means assignment step), and online learning
# (an incremental running mean).
#
# Run with:  Rscript exercise01.R
# Reference solution: solutions/exercise01_solution.R

simple_linear_regression_fit <- function(xs, ys) {
  # TODO: fit y = b0 + b1*x by least squares. Return c(b0, b1).
  #   b1 = sum((x-xbar)*(y-ybar)) / sum((x-xbar)^2)
  #   b0 = ybar - b1*xbar
  stop("TODO: simple_linear_regression_fit")
}

predict_line <- function(xs, b0, b1) {
  # TODO: return b0 + b1*xs (vectorized)
  stop("TODO: predict_line")
}

mse <- function(y_true, y_pred) {
  # TODO: mean((y_true - y_pred)^2)
  stop("TODO: mse")
}

kmeans_assign <- function(points, centroids) {
  # points, centroids: matrices with 2 columns (x, y), one row per point.
  # TODO: for each row of `points`, return the (1-indexed) row index of
  # the nearest row of `centroids` by Euclidean distance.
  stop("TODO: kmeans_assign")
}

online_mean_update <- function(old_mean, new_x, n) {
  # TODO: old_mean + (new_x - old_mean) / n
  stop("TODO: online_mean_update")
}

main <- function() {
  xs <- c(1, 2, 3, 4, 5)
  ys <- c(2.1, 3.9, 6.2, 7.8, 10.1)
  fit <- simple_linear_regression_fit(xs, ys)
  b0 <- fit[1]; b1 <- fit[2]
  preds <- predict_line(xs, b0, b1)
  cat(sprintf("Fitted line: y = %.3f + %.3f x, MSE = %.4f\n", b0, b1, mse(ys, preds)))

  points <- matrix(c(0.0, 0.0, 0.2, 0.1, 5.0, 5.0, 5.1, 4.9), ncol = 2, byrow = TRUE)
  centroids <- matrix(c(0.0, 0.0, 5.0, 5.0), ncol = 2, byrow = TRUE)
  cat("K-means assignments:", kmeans_assign(points, centroids), "\n")

  stream <- c(4.0, 6.0, 8.0, 2.0, 10.0)
  mean_val <- stream[1]
  for (n in 2:length(stream)) {
    mean_val <- online_mean_update(mean_val, stream[n], n)
  }
  cat(sprintf("Final running mean = %.4f (batch mean = %.4f)\n", mean_val, mean(stream)))
}

main()
