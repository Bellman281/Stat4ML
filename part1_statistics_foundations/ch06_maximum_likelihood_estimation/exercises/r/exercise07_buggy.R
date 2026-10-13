# Chapter 6 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# Part I: Statistics Foundation for ML
# level: proof
#
# Two deliberate bugs (score_bernoulli, fisher_information_bernoulli).

score_bernoulli <- function(p, data) {
  # BUG: second term should be SUBTRACTED, not added (Section 2).
  sum(data / p + (1 - data) / (1 - p))
}

fisher_information_bernoulli <- function(p, n) {
  # BUG: Fisher information is n/(p(1-p)), not n*p*(1-p).
  n * p * (1 - p)
}

cramer_rao_lower_bound <- function(p, n) p * (1 - p) / n

mle_variance_sim <- function(p, n, reps, seed = 0) {
  set.seed(seed)
  est <- replicate(reps, mean(rbinom(n, 1, p)))
  m <- mean(est)
  sum((est - m)^2) / reps
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  data <- c(rep(1, 15), rep(0, 35))  # MLE = 0.3
  check("score at MLE (=0)", score_bernoulli(0.3, data), 0.0)
  check("score at p=0.5", score_bernoulli(0.5, data), (15 - 50 * 0.5) / (0.5 * 0.5))
  check("Fisher info(0.3,50)", fisher_information_bernoulli(0.3, 50), 50 / (0.3 * 0.7))
  check("CRLB(0.3,50)", cramer_rao_lower_bound(0.3, 50), 0.3 * 0.7 / 50)
  check("sim var ~ CRLB", mle_variance_sim(0.3, 50, 20000, seed = 0), 0.3 * 0.7 / 50, tol = 4e-4)
  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED\n", length(failures)))
    quit(save = "no", status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
