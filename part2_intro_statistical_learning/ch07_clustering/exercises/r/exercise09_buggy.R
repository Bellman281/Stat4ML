# Chapter 7 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (kpp_weight, silhouette).

kpp_weight <- function(point, chosen) {
  # BUG: k-means++ uses the NEAREST chosen centroid (min), not the farthest.
  max(sapply(chosen, function(c) sum((point - c)^2)))
}
is_core <- function(point, data, eps, min_pts) {
  count <- sum(sapply(data, function(q) sqrt(sum((point - q)^2)) <= eps))
  count >= min_pts
}
silhouette <- function(a, b) {
  # BUG: the silhouette is (b - a) / max(a, b); numerator is reversed here.
  (a - b) / max(a, b)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- if (is.logical(expected)) identical(got, expected) else abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  chosen <- list(c(0, 0), c(5, 5))
  data <- list(c(0, 0), c(1, 0), c(0, 1), c(5, 5))
  check("kpp_weight", kpp_weight(c(4, 4), chosen), 2)
  check("is_core", is_core(c(0, 0), data, 1.5, 3), TRUE)
  check("silhouette", silhouette(2.0, 5.0), 0.6)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
