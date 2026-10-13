# Chapter 2 exercise -- Cross-validation (Research tier)
# level: research
# HOMEWORK: ch02_text.tex Section 3.  Rscript exercise04.R

kfold_split_sizes <- function(n, k) {
  # TODO: k fold sizes summing to n; first (n mod k) folds get one extra
  stop("TODO: kfold_split_sizes")
}
mean_cv_error <- function(fold_errors) {
  # TODO: mean of the per-fold errors
  stop("TODO: mean_cv_error")
}
loocv_from_leverage <- function(residuals, leverages) {
  # TODO: mean( (e_i / (1 - h_i))^2 )
  stop("TODO: loocv_from_leverage")
}

main <- function() {
  cat("fold sizes   :", kfold_split_sizes(10, 3), "\n")
  cat("mean cv err  :", mean_cv_error(c(0.1, 0.2, 0.3)), "\n")
  cat("loocv        :", loocv_from_leverage(c(1, 1), c(0.5, 0.5)), "\n")
}
main()
