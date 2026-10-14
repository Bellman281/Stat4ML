# Chapter 2 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (bernoulli_score, mle_mean).

gaussian_score <- function(y, mu, sigma2) (y - mu) / sigma2
bernoulli_score <- function(y, p) {
  # BUG: the score is (y - p) / (p(1-p)); this divides by p only.
  (y - p) / p
}
mle_mean <- function(ys) {
  # BUG: the score equation solves to the MEAN, not the sum.
  sum(ys)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  ys <- c(2.0, 4.0, 6.0)
  check("gaussian_score", gaussian_score(3.0, 1.0, 2.0), 1.0)
  check("bernoulli_score", bernoulli_score(1, 0.5), 2.0)
  check("mle_mean", mle_mean(ys), 4.0)
  check("score zero at mle", sum(sapply(ys, function(y) gaussian_score(y, mle_mean(ys), 1.0))), 0.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
