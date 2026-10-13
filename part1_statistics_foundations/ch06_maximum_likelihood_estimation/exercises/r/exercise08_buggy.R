# Chapter 6 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# Part I: Statistics Foundation for ML
# level: research
#
# Two deliberate bugs (avg_negloglik, sandwich_variance).

avg_negloglik <- function(theta, data) {
  # BUG: SUMS the per-observation NLL instead of AVERAGING it (Section 3).
  sum(0.5 * (data - theta)^2 + 0.5 * log(2 * pi))
}

fisher_scoring_mean <- function(data, init, iters) {
  n <- length(data)
  theta <- init
  for (i in seq_len(iters)) theta <- theta + sum(data - theta) / n
  theta
}

naive_variance <- function(data) 1 / length(data)

sandwich_variance <- function(data, theta) {
  # BUG: sandwich is A^{-1} B A^{-1}; divide by A twice (n^2), not once.
  n <- length(data)
  B <- sum((data - theta)^2)
  B / n
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  data <- c(1, 3, 2, 6, 4, 2, 5, 1)  # mean 3.0, SS about mean 24
  check("fisher_scoring -> mean", fisher_scoring_mean(data, 0.0, 1), 3.0)
  check("avg NLL at 3.0", avg_negloglik(3.0, data), 0.5 * 3.0 + 0.5 * log(2 * pi))
  check("naive var", naive_variance(data), 1 / 8)
  check("sandwich var", sandwich_variance(data, 3.0), 24 / (8^2))
  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED\n", length(failures)))
    quit(save = "no", status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
