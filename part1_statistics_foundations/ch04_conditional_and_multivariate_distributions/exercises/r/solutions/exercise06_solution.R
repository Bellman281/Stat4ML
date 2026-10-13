# Chapter 4 -- reference solution (Research, R)
# level: research
bvn_conditional_mean <- function(mu_y, rho, sy, sx, x, mu_x) mu_y + rho * (sy / sx) * (x - mu_x)
bvn_conditional_var <- function(sy, rho) sy^2 * (1 - rho^2)
mvn_conditional_mean_1d <- function(mu1, s12, s22, x2, mu2) mu1 + (s12 / s22) * (x2 - mu2)
main <- function() {
  cat("E[Y|X=2]      :", bvn_conditional_mean(0.0, 0.7, 2.0, 1.0, 2.0, 0.0), "\n")
  cat("Var(Y|X)      :", bvn_conditional_var(2.0, 0.7), "\n")
  cat("MVN cond mean :", mvn_conditional_mean_1d(0.0, 0.7, 1.0, 2.0, 0.0), "\n")
}
main()
