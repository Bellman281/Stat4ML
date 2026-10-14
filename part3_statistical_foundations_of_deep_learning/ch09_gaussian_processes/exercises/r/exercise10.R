# Chapter 9 exercise -- the GP posterior at one point (Proof tier)
# level: proof
# HOMEWORK: ch09_text.tex Section 2.  Rscript exercise10.R

gp_post_mean <- function(k_star, k_11, sigma2, y) {
  # TODO: k_star / (k_11 + sigma2) * y
  stop("TODO: gp_post_mean")
}
gp_post_var <- function(k_ss, k_star, k_11, sigma2) {
  # TODO: k_ss - k_star^2 / (k_11 + sigma2)
  stop("TODO: gp_post_var")
}

main <- function() {
  cat("gp_post_mean :", gp_post_mean(0.6, 1.0, 0.1, 2.0), "\n")
  cat("gp_post_var  :", gp_post_var(1.0, 0.6, 1.0, 0.1), "\n")
  cat("var at data  :", gp_post_var(1.0, 1.0, 1.0, 0.0), "\n")
}
main()
