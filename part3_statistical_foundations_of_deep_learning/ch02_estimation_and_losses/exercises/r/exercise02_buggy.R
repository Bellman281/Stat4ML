# Chapter 2 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (bernoulli_nll, gaussian_nll).

mse <- function(preds, targets) mean((preds - targets)^2)
bernoulli_nll <- function(p, y) {
  # BUG: it is the NEGATIVE log-likelihood; the leading minus is missing.
  y * log(p) + (1 - y) * log(1 - p)
}
gaussian_nll <- function(mu, ys, sigma) {
  n <- length(ys)
  # BUG: the quadratic term is divided by 2*sigma^2, not 2*sigma.
  n / 2 * log(2 * pi * sigma^2) + sum((ys - mu)^2) / (2 * sigma)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("mse", mse(c(1, 2, 3), c(1, 2, 5)), 4 / 3)
  check("bernoulli_nll", bernoulli_nll(0.8, 1), -log(0.8))
  eg <- 2 / 2 * log(2 * pi * 4) + (1 + 1) / (2 * 4)
  check("gaussian_nll", gaussian_nll(0.0, c(1.0, -1.0), 2.0), eg)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
