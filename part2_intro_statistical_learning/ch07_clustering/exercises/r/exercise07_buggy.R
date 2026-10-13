# Chapter 7 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (nearest, centroid).

sq_dist <- function(a, b) sum((a - b)^2)
nearest <- function(point, centroids) {
  # BUG: the nearest centroid minimises distance -> which.min, not which.max.
  which.max(sapply(centroids, function(c) sq_dist(point, c)))
}
centroid <- function(points) {
  n <- length(points)
  mx <- sum(sapply(points, function(p) p[1])) / n
  # BUG: the y-mean averages p[2], not p[1].
  my <- sum(sapply(points, function(p) p[1])) / n
  c(mx, my)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- length(got) == length(expected) && all(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name,
                paste(format(got), collapse = ","),
                paste(format(expected), collapse = ",")))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  cs <- list(c(0, 0), c(5, 5))
  check("sq_dist", sq_dist(c(0, 0), c(3, 4)), 25)
  check("nearest", nearest(c(4, 4), cs), 2)
  check("centroid", centroid(list(c(0, 0), c(2, 0), c(1, 6))), c(1, 2))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
