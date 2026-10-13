# Chapter 2 exercise -- Bias-variance decomposition (Proof tier)
# level: proof
# HOMEWORK: ch02_text.tex Section 2.  Rscript exercise03.R

squared_bias <- function(preds, truth) {
  # TODO: (mean(preds) - truth)^2
  stop("TODO: squared_bias")
}
estimator_variance <- function(preds) {
  # TODO: population variance mean((p - mean(preds))^2)
  stop("TODO: estimator_variance")
}
expected_mse <- function(preds, truth) {
  # TODO: mean((p - truth)^2)
  stop("TODO: expected_mse")
}

main <- function() {
  preds <- c(2, 4, 6); truth <- 5
  cat("bias^2   :", squared_bias(preds, truth), "\n")
  cat("variance :", estimator_variance(preds), "\n")
  cat("MSE      :", expected_mse(preds, truth), "\n")
}
main()
