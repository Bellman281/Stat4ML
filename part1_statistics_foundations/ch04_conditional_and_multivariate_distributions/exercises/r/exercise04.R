# Chapter 4 exercise -- Joint, marginal, conditional (Core)
# level: core
# joint is a list(x=, y=, p=) describing P(X=x, Y=y) row by row.
# Rscript exercise04.R

JOINT <- list(x = c(0, 0, 1, 1), y = c(0, 1, 0, 1), p = c(0.3, 0.2, 0.1, 0.4))

marginal_x_prob <- function(joint, x0) {
  # TODO: sum of p over rows with x == x0
  stop("TODO: marginal_x_prob")
}
conditional_y_prob <- function(joint, y0, x0) {
  # TODO: P(X=x0, Y=y0) / P(X=x0)
  stop("TODO: conditional_y_prob")
}
joint_covariance <- function(joint) {
  # TODO: E[XY] - E[X]E[Y]
  stop("TODO: joint_covariance")
}

main <- function() {
  cat("P(X=0)        :", marginal_x_prob(JOINT, 0), "\n")
  cat("P(Y=1 | X=0)  :", conditional_y_prob(JOINT, 1, 0), "\n")
  cat("P(Y=1 | X=1)  :", conditional_y_prob(JOINT, 1, 1), "\n")
  cat("Cov(X,Y)      :", joint_covariance(JOINT), "\n")
}
main()
