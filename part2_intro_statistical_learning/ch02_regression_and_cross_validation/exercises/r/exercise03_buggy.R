# Chapter 2 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (squared_bias, estimator_variance).

squared_bias <- function(preds, truth) {
  # BUG: bias is SQUARED -- (mean - truth)^2, not (mean - truth).
  mean(preds) - truth
}
estimator_variance <- function(preds) {
  # BUG: population variance divides by n, not n-1.
  m <- mean(preds); sum((preds - m)^2) / (length(preds) - 1)
}
expected_mse <- function(preds, truth) mean((preds - truth)^2)

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- length(got) == length(expected) && all(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  preds <- c(2, 4, 6); truth <- 5
  check("squared_bias", squared_bias(preds, truth), 1.0)
  check("estimator_variance", estimator_variance(preds), 8/3)
  check("expected_mse", expected_mse(preds, truth), 11/3)
  check("identity", squared_bias(preds, truth) + estimator_variance(preds), 11/3)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
