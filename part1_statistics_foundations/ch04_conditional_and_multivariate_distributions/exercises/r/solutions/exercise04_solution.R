# Chapter 4 -- reference solution (Core, R)
# level: core
JOINT <- list(x = c(0, 0, 1, 1), y = c(0, 1, 0, 1), p = c(0.3, 0.2, 0.1, 0.4))
marginal_x_prob <- function(joint, x0) sum(joint$p[joint$x == x0])
conditional_y_prob <- function(joint, y0, x0) {
  num <- sum(joint$p[joint$x == x0 & joint$y == y0])
  num / marginal_x_prob(joint, x0)
}
joint_covariance <- function(joint) {
  ex <- sum(joint$x * joint$p); ey <- sum(joint$y * joint$p)
  exy <- sum(joint$x * joint$y * joint$p)
  exy - ex * ey
}
main <- function() {
  cat("P(X=0)        :", marginal_x_prob(JOINT, 0), "\n")
  cat("P(Y=1 | X=0)  :", conditional_y_prob(JOINT, 1, 0), "\n")
  cat("P(Y=1 | X=1)  :", conditional_y_prob(JOINT, 1, 1), "\n")
  cat("Cov(X,Y)      :", joint_covariance(JOINT), "\n")
}
main()
