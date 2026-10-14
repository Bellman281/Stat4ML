# Chapter 6 -- reference solution (Core, R)
# level: core
discounted_return <- function(rewards, gamma) sum(gamma^(seq_along(rewards) - 1) * rewards)
q_backup <- function(r, gamma, next_values, probs) r + gamma * sum(probs * next_values)
greedy_action <- function(q_values) which.max(q_values)
main <- function() {
  cat("discounted_return :", discounted_return(c(1, 1, 1), 0.5), "\n")
  cat("q_backup          :", q_backup(0.0, 0.9, c(10.0, 0.0), c(0.8, 0.2)), "\n")
  cat("greedy_action     :", greedy_action(c(1.0, 5.0, 3.0)), "\n")
}
main()
