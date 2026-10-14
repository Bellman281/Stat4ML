# Chapter 10 exercise -- conformal and calibration primitives (Core tier)
# level: core
# HOMEWORK: ch10_text.tex Sections 1-2.  Rscript exercise10.R

nonconformity <- function(y, pred) {
  # TODO: abs(y - pred)
  stop("TODO: nonconformity")
}
quantile_rank <- function(n, alpha) {
  # TODO: ceiling((n + 1) * (1 - alpha))
  stop("TODO: quantile_rank")
}
coverage <- function(ys, preds, q) {
  # TODO: mean(abs(ys - preds) <= q)
  stop("TODO: coverage")
}

main <- function() {
  cat("nonconformity :", nonconformity(3.0, 2.5), "\n")
  cat("quantile_rank :", quantile_rank(99, 0.1), "\n")
  cat("coverage      :", coverage(c(1.0, 2.0, 3.0), c(1.0, 2.0, 5.0), 1.0), "\n")
}
main()
