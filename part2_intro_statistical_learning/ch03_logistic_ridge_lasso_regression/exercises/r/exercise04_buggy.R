# Chapter 3 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (ridge_estimator_1d, soft_threshold).

ridge_estimator_1d <- function(x, y, lam) {
  # BUG: ridge adds lam to the denominator (Sxx + lam); it's forgotten here.
  sxy <- sum((x - mean(x)) * (y - mean(y))); sxx <- sum((x - mean(x))^2)
  sxy / sxx
}
soft_threshold <- function(z, lam) {
  # BUG: this drops the sign, so negative z comes out positive.
  max(abs(z) - lam, 0)
}
sigmoid_prime <- function(z) { s <- 1 / (1 + exp(-z)); s * (1 - s) }

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  x <- c(1, 2, 3); y <- c(2, 4, 6)
  check("ridge (lam=2)", ridge_estimator_1d(x, y, 2.0), 1.0)
  check("soft_threshold(-2,1)", soft_threshold(-2.0, 1.0), -1.0)
  check("soft_threshold(0.5,1)", soft_threshold(0.5, 1.0), 0.0)
  check("sigmoid_prime(0)", sigmoid_prime(0.0), 0.25)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
