# Chapter 6 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (discounted_return, greedy_action).

discounted_return <- function(rewards, gamma) {
  # BUG: step t is discounted by gamma^t with t starting at 0; this starts at 1.
  sum(gamma^seq_along(rewards) * rewards)
}
q_backup <- function(r, gamma, next_values, probs) r + gamma * sum(probs * next_values)
greedy_action <- function(q_values) {
  # BUG: the greedy action MAXIMISES the Q-value; use which.max, not which.min.
  which.min(q_values)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("discounted_return", discounted_return(c(1, 1, 1), 0.5), 1 + 0.5 + 0.25)
  check("q_backup", q_backup(0.0, 0.9, c(10.0, 0.0), c(0.8, 0.2)), 7.2)
  check("greedy_action", greedy_action(c(1.0, 5.0, 3.0)), 2)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
