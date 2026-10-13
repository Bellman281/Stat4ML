# Chapter 6 -- reference solution (Research, R)
# level: research
hard_assignment <- function(resp) which.max(resp)
responsibility_based_weight <- function(resp_column) mean(resp_column)
em_lower_bound_gap <- function(ll_before, ll_after) ll_after - ll_before
main <- function() {
  cat("hard_assignment :", hard_assignment(c(0.2, 0.7, 0.1)), "\n")
  cat("weight          :", responsibility_based_weight(c(0.5, 0.5, 1.0, 0.0)), "\n")
  cat("em gap          :", em_lower_bound_gap(1.0, 1.5), "\n")
}
main()
