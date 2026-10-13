# Chapter 2 -- reference solution (Proof, R)
# level: proof
squared_bias <- function(preds, truth) (mean(preds) - truth)^2
estimator_variance <- function(preds) { m <- mean(preds); sum((preds - m)^2) / length(preds) }
expected_mse <- function(preds, truth) mean((preds - truth)^2)
main <- function() {
  preds <- c(2, 4, 6); truth <- 5
  cat("bias^2   :", squared_bias(preds, truth), "\n")
  cat("variance :", estimator_variance(preds), "\n")
  cat("MSE      :", expected_mse(preds, truth), "\n")
}
main()
