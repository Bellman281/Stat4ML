# Chapter 10 -- reference solution (Core, R)
# level: core
nonconformity <- function(y, pred) abs(y - pred)
quantile_rank <- function(n, alpha) ceiling((n + 1) * (1 - alpha))
coverage <- function(ys, preds, q) mean(abs(ys - preds) <= q)
main <- function() {
  cat("nonconformity :", nonconformity(3.0, 2.5), "\n")
  cat("quantile_rank :", quantile_rank(99, 0.1), "\n")
  cat("coverage      :", coverage(c(1.0, 2.0, 3.0), c(1.0, 2.0, 5.0), 1.0), "\n")
}
main()
