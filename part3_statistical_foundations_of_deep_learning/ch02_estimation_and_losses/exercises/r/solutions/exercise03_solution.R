# Chapter 2 -- reference solution (Proof, R)
# level: proof
gaussian_log_prior <- function(w, tau) -w^2 / (2 * tau^2)
ridge_lambda <- function(sigma2, tau2) sigma2 / tau2
ridge_estimate_1d <- function(xs, ys, lam) sum(xs * ys) / (sum(xs^2) + lam)
main <- function() {
  xs <- c(1, 2, 3); ys <- c(2, 4, 6)
  cat("gaussian_log_prior:", gaussian_log_prior(2.0, 1.0), "\n")
  cat("ridge_lambda      :", ridge_lambda(1.0, 0.5), "\n")
  cat("ridge (lam=0, OLS):", ridge_estimate_1d(xs, ys, 0.0), "\n")
  cat("ridge (lam=14)    :", ridge_estimate_1d(xs, ys, 14.0), "\n")
}
main()
