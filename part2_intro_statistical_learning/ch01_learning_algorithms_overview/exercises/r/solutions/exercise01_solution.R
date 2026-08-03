# Chapter 1 (Part II) -- reference solution (R)

simple_linear_regression_fit <- function(xs, ys) {
  xbar <- mean(xs); ybar <- mean(ys)
  b1 <- sum((xs - xbar) * (ys - ybar)) / sum((xs - xbar)^2)
  b0 <- ybar - b1 * xbar
  c(b0, b1)
}

predict_line <- function(xs, b0, b1) {
  b0 + b1 * xs
}

mse <- function(y_true, y_pred) {
  mean((y_true - y_pred)^2)
}

kmeans_assign <- function(points, centroids) {
  n <- nrow(points)
  k <- nrow(centroids)
  assignments <- integer(n)
  for (i in seq_len(n)) {
    dists <- sqrt(rowSums((matrix(rep(points[i, ], k), nrow = k, byrow = TRUE) - centroids)^2))
    assignments[i] <- which.min(dists)
  }
  assignments
}

online_mean_update <- function(old_mean, new_x, n) {
  old_mean + (new_x - old_mean) / n
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
