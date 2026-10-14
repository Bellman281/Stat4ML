# Chapter 1 -- reference solution (Core, R)
# level: core
zero_one_loss <- function(pred, y) if (pred != y) 1 else 0
empirical_risk <- function(preds, ys) mean(mapply(zero_one_loss, preds, ys))
generalisation_gap <- function(emp_risk, true_risk) true_risk - emp_risk
main <- function() {
  preds <- c(1, 0, 1, 1); ys <- c(1, 1, 1, 0)
  cat("zero_one(1,1) :", zero_one_loss(1, 1), "\n")
  cat("zero_one(1,0) :", zero_one_loss(1, 0), "\n")
  cat("empirical_risk:", empirical_risk(preds, ys), "\n")
  cat("gap(0.3,0.5)  :", generalisation_gap(0.3, 0.5), "\n")
}
main()
