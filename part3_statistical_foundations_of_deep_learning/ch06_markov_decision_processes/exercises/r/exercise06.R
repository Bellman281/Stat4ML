# Chapter 6 exercise -- MDP value backups (Core tier)
# level: core
# HOMEWORK: ch06_text.tex Sections 1-2.  Rscript exercise06.R
# NOTE: R indices are 1-based, so greedy_action returns a 1-based index.

discounted_return <- function(rewards, gamma) {
  # TODO: sum of gamma^t * rewards[t], with t starting at 0
  stop("TODO: discounted_return")
}
q_backup <- function(r, gamma, next_values, probs) {
  # TODO: r + gamma * sum(probs * next_values)
  stop("TODO: q_backup")
}
greedy_action <- function(q_values) {
  # TODO: index (1-based) of the maximum Q-value; use which.max
  stop("TODO: greedy_action")
}

main <- function() {
  cat("discounted_return :", discounted_return(c(1, 1, 1), 0.5), "\n")
  cat("q_backup          :", q_backup(0.0, 0.9, c(10.0, 0.0), c(0.8, 0.2)), "\n")
  cat("greedy_action     :", greedy_action(c(1.0, 5.0, 3.0)), "\n")
}
main()
