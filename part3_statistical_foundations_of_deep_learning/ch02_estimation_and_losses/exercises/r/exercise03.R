# Chapter 2 exercise -- MAP = penalised MLE (Proof tier)
# level: proof
# HOMEWORK: ch02_text.tex Section 2.  Rscript exercise03.R

gaussian_log_prior <- function(w, tau) {
  # TODO: -w^2 / (2 * tau^2)
  stop("TODO: gaussian_log_prior")
}
ridge_lambda <- function(sigma2, tau2) {
  # TODO: sigma2 / tau2
  stop("TODO: ridge_lambda")
}
ridge_estimate_1d <- function(xs, ys, lam) {
  # TODO: sum(xs*ys) / (sum(xs^2) + lam)
  stop("TODO: ridge_estimate_1d")
}

main <- function() {
  xs <- c(1, 2, 3); ys <- c(2, 4, 6)
  cat("gaussian_log_prior:", gaussian_log_prior(2.0, 1.0), "\n")
  cat("ridge_lambda      :", ridge_lambda(1.0, 0.5), "\n")
  cat("ridge (lam=0, OLS):", ridge_estimate_1d(xs, ys, 0.0), "\n")
  cat("ridge (lam=14)    :", ridge_estimate_1d(xs, ys, 14.0), "\n")
}
main()
