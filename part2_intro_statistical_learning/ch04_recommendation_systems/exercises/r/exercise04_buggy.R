# Chapter 4 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (squared_error, rmse). Do not edit run_tests().

predict_rating <- function(p, q) sum(p * q)

squared_error <- function(r, p, q) {
  # BUG: returns the raw residual, not its SQUARE. The objective sums
  # (r - p.q)^2 (ch04_text.tex Section 2), so the error must be squared.
  r - predict_rating(p, q)
}

rmse <- function(preds, actuals) {
  mse <- mean((preds - actuals)^2)
  # BUG: RMSE is the *root* mean squared error -- take the square root.
  mse
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("predict", predict_rating(c(1, 2), c(2, 0.5)), 3.0)
  check("squared_error", squared_error(5, c(1, 2), c(2, 0.5)), 4.0)
  check("rmse", rmse(c(3, 2, 5), c(4, 2, 4)), sqrt(2 / 3))
  check("rmse_zero", rmse(c(2, 2), c(2, 2)), 0.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
