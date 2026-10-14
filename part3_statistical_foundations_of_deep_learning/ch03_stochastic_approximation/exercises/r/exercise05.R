# Chapter 3 exercise -- noise ball, stability, averaging (Research tier)
# level: research
# HOMEWORK: ch03_text.tex Sections 2-3.  Rscript exercise05.R

ou_stationary_var <- function(lr, sigma2, H) {
  # TODO: lr * sigma2 / (2 * H)
  stop("TODO: ou_stationary_var")
}
critical_lr <- function(H) {
  # TODO: 2 / H
  stop("TODO: critical_lr")
}
polyak_var <- function(stationary_var, k) {
  # TODO: stationary_var / k
  stop("TODO: polyak_var")
}

main <- function() {
  v <- ou_stationary_var(0.1, 1.0, 2.0)
  cat("ou_stationary_var:", v, "\n")
  cat("critical_lr      :", critical_lr(2.0), "\n")
  cat("polyak_var (k=10):", polyak_var(v, 10), "\n")
}
main()
