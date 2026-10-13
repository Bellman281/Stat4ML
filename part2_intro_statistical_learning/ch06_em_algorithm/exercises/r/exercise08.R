# Chapter 6 exercise -- Hard EM and monotonicity (Research tier)
# level: research
# HOMEWORK: ch06_text.tex Section 3.  Rscript exercise08.R
# hard_assignment returns a 1-based index (R convention).

hard_assignment <- function(resp) {
  # TODO: index of the largest responsibility (which.max)
  stop("TODO: hard_assignment")
}
responsibility_based_weight <- function(resp_column) {
  # TODO: mean of a component's responsibilities
  stop("TODO: responsibility_based_weight")
}
em_lower_bound_gap <- function(ll_before, ll_after) {
  # TODO: ll_after - ll_before
  stop("TODO: em_lower_bound_gap")
}

main <- function() {
  cat("hard_assignment :", hard_assignment(c(0.2, 0.7, 0.1)), "\n")
  cat("weight          :", responsibility_based_weight(c(0.5, 0.5, 1.0, 0.0)), "\n")
  cat("em gap          :", em_lower_bound_gap(1.0, 1.5), "\n")
}
main()
