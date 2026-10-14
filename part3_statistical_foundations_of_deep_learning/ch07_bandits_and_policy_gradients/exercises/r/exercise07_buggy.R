# Chapter 7 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (ucb_index, cumulative_regret).

ucb_index <- function(mean, n, t, c) {
  # BUG: the bonus is sqrt(c log t / n); the sqrt is missing.
  mean + c * log(t) / n
}
argmax_index <- function(values) which.max(values)
cumulative_regret <- function(mu_star, chosen_means) {
  # BUG: regret per round is (mu_star - chosen), not (chosen - mu_star).
  sum(chosen_means - mu_star)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("ucb_index", ucb_index(0.5, 4, 100, 2.0), 0.5 + sqrt(2.0 * log(100) / 4))
  check("argmax_index", argmax_index(c(1.0, 5.0, 3.0)), 2)
  check("cumulative_regret", cumulative_regret(1.0, c(0.8, 0.9, 1.0)),
        (1.0 - 0.8) + (1.0 - 0.9) + (1.0 - 1.0))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
