# Chapter 6 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# Part I: Statistics Foundation for ML
# level: core
#
# Two deliberate bugs (bernoulli_loglik, normal_mle). Fix one function at a
# time until you see "All tests passed!". Do not edit run_tests().

bernoulli_loglik <- function(p, data) {
  # BUG: drops the (1-x)*log(1-p) term -- only counts successes.
  sum(data * log(p))
}

bernoulli_mle <- function(data) mean(data)

poisson_mle <- function(data) mean(data)

normal_mle <- function(data) {
  # BUG: MLE sigma^2 divides by n, not n-1 (editorial note, Section 1).
  n <- length(data)
  mu <- sum(data) / n
  sigma2 <- sum((data - mu)^2) / (n - 1)
  c(mu, sigma2)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  b <- c(1, 1, 0, 1, 0, 1, 0, 0, 1, 1)
  check("bernoulli_mle", bernoulli_mle(b), 0.6)
  check("bernoulli_loglik(0.6)", bernoulli_loglik(0.6, b), 6 * log(0.6) + 4 * log(0.4))
  check("poisson_mle", poisson_mle(c(2, 1, 3, 0, 2, 1, 4, 2)), 1.875)
  nm <- normal_mle(c(2, 4, 4, 4, 5, 5, 7, 9))
  check("normal_mle mu", nm[1], 5.0)
  check("normal_mle sigma2 (/n)", nm[2], 4.0)
  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED\n", length(failures)))
    quit(save = "no", status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
