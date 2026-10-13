# Chapter 7 -- reference solution (Research, R)
# level: research
kpp_weight <- function(point, chosen) min(sapply(chosen, function(c) sum((point - c)^2)))
is_core <- function(point, data, eps, min_pts) {
  sum(sapply(data, function(q) sqrt(sum((point - q)^2)) <= eps)) >= min_pts
}
silhouette <- function(a, b) (b - a) / max(a, b)
main <- function() {
  chosen <- list(c(0, 0), c(5, 5))
  data <- list(c(0, 0), c(1, 0), c(0, 1), c(5, 5))
  cat("kpp_weight :", kpp_weight(c(4, 4), chosen), "\n")
  cat("is_core    :", is_core(c(0, 0), data, 1.5, 3), "\n")
  cat("silhouette :", silhouette(2.0, 5.0), "\n")
}
main()
