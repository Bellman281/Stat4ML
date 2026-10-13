# Chapter 7 exercise -- seeding, density, and validity (Research tier)
# level: research
# HOMEWORK: ch07_text.tex Sections 2-3.  Rscript exercise09.R
# Points are numeric vectors c(x, y); a set is a list of them.

kpp_weight <- function(point, chosen) {
  # TODO: k-means++ weight = squared distance to the NEAREST chosen centroid
  stop("TODO: kpp_weight")
}
is_core <- function(point, data, eps, min_pts) {
  # TODO: TRUE iff >= min_pts points of `data` lie within distance eps of point
  stop("TODO: is_core")
}
silhouette <- function(a, b) {
  # TODO: (b - a) / max(a, b)
  stop("TODO: silhouette")
}

main <- function() {
  chosen <- list(c(0, 0), c(5, 5))
  data <- list(c(0, 0), c(1, 0), c(0, 1), c(5, 5))
  cat("kpp_weight :", kpp_weight(c(4, 4), chosen), "\n")
  cat("is_core    :", is_core(c(0, 0), data, 1.5, 3), "\n")
  cat("silhouette :", silhouette(2.0, 5.0), "\n")
}
main()
