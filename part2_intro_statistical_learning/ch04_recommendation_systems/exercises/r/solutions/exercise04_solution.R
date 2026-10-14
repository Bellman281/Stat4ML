# Chapter 4 -- reference solution (Core, R)
# level: core
predict_rating <- function(p, q) sum(p * q)
squared_error <- function(r, p, q) {
  e <- r - predict_rating(p, q)
  e * e
}
rmse <- function(preds, actuals) sqrt(mean((preds - actuals)^2))
main <- function() {
  cat("predict       :", predict_rating(c(1, 2), c(2, 0.5)), "\n")
  cat("squared_error :", squared_error(5, c(1, 2), c(2, 0.5)), "\n")
  cat("rmse          :", rmse(c(3, 2, 5), c(4, 2, 4)), "\n")
}
main()
