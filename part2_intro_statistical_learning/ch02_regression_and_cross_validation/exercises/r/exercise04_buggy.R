# Chapter 2 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (kfold_split_sizes, loocv_from_leverage).

kfold_split_sizes <- function(n, k) {
  # BUG: this drops the remainder so the sizes don't sum to n; the first
  # (n mod k) folds must get one extra point.
  base <- n %/% k
  rep(base, k)
}
mean_cv_error <- function(fold_errors) mean(fold_errors)
loocv_from_leverage <- function(residuals, leverages) {
  # BUG: each leave-one-out residual e_i/(1-h_i) is SQUARED before averaging.
  mean(residuals / (1 - leverages))
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- length(got) == length(expected) && all(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, paste(format(got), collapse=","), paste(format(expected), collapse=",")))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("kfold_split_sizes", kfold_split_sizes(10, 3), c(4, 3, 3))
  check("kfold sizes sum", sum(kfold_split_sizes(10, 3)), 10)
  check("mean_cv_error", mean_cv_error(c(0.1, 0.2, 0.3)), 0.2)
  check("loocv_from_leverage", loocv_from_leverage(c(1, 1), c(0.5, 0.5)), 4.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
