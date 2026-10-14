# Chapter 9 -- reference solution (Proof, R)
# level: proof
gp_post_mean <- function(k_star, k_11, sigma2, y) k_star / (k_11 + sigma2) * y
gp_post_var <- function(k_ss, k_star, k_11, sigma2) k_ss - k_star^2 / (k_11 + sigma2)
main <- function() {
  cat("gp_post_mean :", gp_post_mean(0.6, 1.0, 0.1, 2.0), "\n")
  cat("gp_post_var  :", gp_post_var(1.0, 0.6, 1.0, 0.1), "\n")
  cat("var at data  :", gp_post_var(1.0, 1.0, 1.0, 0.0), "\n")
}
main()
