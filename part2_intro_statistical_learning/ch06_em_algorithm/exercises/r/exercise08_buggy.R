# Chapter 6 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (hard_assignment, responsibility_based_weight).

hard_assignment <- function(resp) {
  # BUG: the hard assignment is the ARGMAX, not the argmin.
  which.min(resp)
}
responsibility_based_weight <- function(resp_column) {
  # BUG: the mixing weight is the MEAN of the responsibilities, not the sum.
  sum(resp_column)
}
em_lower_bound_gap <- function(ll_before, ll_after) ll_after - ll_before

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("hard_assignment", hard_assignment(c(0.2, 0.7, 0.1)), 2)
  check("weight (mean)", responsibility_based_weight(c(0.5, 0.5, 1.0, 0.0)), 0.5)
  check("em_lower_bound_gap", em_lower_bound_gap(1.0, 1.5), 0.5)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
