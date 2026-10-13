# Chapter 4 exercise -- Conditioning the normal (Research tier)
# level: research
# HOMEWORK: ch04_text.tex Section 3.  Rscript exercise06.R

bvn_conditional_mean <- function(mu_y, rho, sy, sx, x, mu_x) {
  # TODO: mu_y + rho * (sy/sx) * (x - mu_x)
  stop("TODO: bvn_conditional_mean")
}
bvn_conditional_var <- function(sy, rho) {
  # TODO: sy^2 * (1 - rho^2)
  stop("TODO: bvn_conditional_var")
}
mvn_conditional_mean_1d <- function(mu1, s12, s22, x2, mu2) {
  # TODO: mu1 + (s12/s22) * (x2 - mu2)
  stop("TODO: mvn_conditional_mean_1d")
}

main <- function() {
  cat("E[Y|X=2]      :", bvn_conditional_mean(0.0, 0.7, 2.0, 1.0, 2.0, 0.0), "\n")
  cat("Var(Y|X)      :", bvn_conditional_var(2.0, 0.7), "\n")
  cat("MVN cond mean :", mvn_conditional_mean_1d(0.0, 0.7, 1.0, 2.0, 0.0), "\n")
}
main()
