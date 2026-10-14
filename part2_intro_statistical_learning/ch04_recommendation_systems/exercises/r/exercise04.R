# Chapter 4 exercise -- the latent-factor prediction (Core tier, R)
# level: core
# HOMEWORK: ch04_text.tex Section 1.  Rscript exercise04.R
# A rating is the dot product of a user factor and an item factor.
# RMSE = *root* mean squared error.

predict_rating <- function(p, q) {
  # TODO: dot product sum(p * q)
  stop("TODO: predict_rating")
}
squared_error <- function(r, p, q) {
  # TODO: (r - p.q)^2
  stop("TODO: squared_error")
}
rmse <- function(preds, actuals) {
  # TODO: sqrt(mean((preds - actuals)^2))
  stop("TODO: rmse")
}

main <- function() {
  cat("predict       :", predict_rating(c(1, 2), c(2, 0.5)), "\n")
  cat("squared_error :", squared_error(5, c(1, 2), c(2, 0.5)), "\n")
  cat("rmse          :", rmse(c(3, 2, 5), c(4, 2, 4)), "\n")
}
main()
