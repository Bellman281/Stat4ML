# Chapter 2 -- reference solution (Research, R)
# level: research
kfold_split_sizes <- function(n, k) {
  base <- n %/% k; rem <- n %% k
  c(rep(base + 1, rem), rep(base, k - rem))
}
mean_cv_error <- function(fold_errors) mean(fold_errors)
loocv_from_leverage <- function(residuals, leverages) mean((residuals / (1 - leverages))^2)
main <- function() {
  cat("fold sizes   :", kfold_split_sizes(10, 3), "\n")
  cat("mean cv err  :", mean_cv_error(c(0.1, 0.2, 0.3)), "\n")
  cat("loocv        :", loocv_from_leverage(c(1, 1), c(0.5, 0.5)), "\n")
}
main()
