# Chapter 1 exercise -- risk and the generalisation gap (Core tier)
# level: core
# HOMEWORK: ch01_text.tex Section 1.  Rscript exercise01.R

zero_one_loss <- function(pred, y) {
  # TODO: 0 if correct, 1 if wrong
  stop("TODO: zero_one_loss")
}
empirical_risk <- function(preds, ys) {
  # TODO: mean 0-1 loss over the sample
  stop("TODO: empirical_risk")
}
generalisation_gap <- function(emp_risk, true_risk) {
  # TODO: R - Rhat = true_risk - emp_risk
  stop("TODO: generalisation_gap")
}

main <- function() {
  preds <- c(1, 0, 1, 1); ys <- c(1, 1, 1, 0)
  cat("zero_one(1,1) :", zero_one_loss(1, 1), "\n")
  cat("zero_one(1,0) :", zero_one_loss(1, 0), "\n")
  cat("empirical_risk:", empirical_risk(preds, ys), "\n")
  cat("gap(0.3,0.5)  :", generalisation_gap(0.3, 0.5), "\n")
}
main()
