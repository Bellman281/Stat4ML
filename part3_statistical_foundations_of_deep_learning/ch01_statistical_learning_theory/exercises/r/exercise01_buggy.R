# Chapter 1 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (zero_one_loss, generalisation_gap).

zero_one_loss <- function(pred, y) {
  # BUG: 0-1 loss is 1 when WRONG, 0 when correct; this is reversed.
  if (pred != y) 0 else 1
}
empirical_risk <- function(preds, ys) {
  mean(mapply(zero_one_loss, preds, ys))
}
generalisation_gap <- function(emp_risk, true_risk) {
  # BUG: the gap is true_risk - emp_risk, not emp_risk - true_risk.
  emp_risk - true_risk
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("zero_one_correct", zero_one_loss(1, 1), 0)
  check("zero_one_wrong", zero_one_loss(1, 0), 1)
  check("empirical_risk", empirical_risk(c(1, 0, 1, 1), c(1, 1, 1, 0)), 0.5)
  check("gap", generalisation_gap(0.3, 0.5), 0.2)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
