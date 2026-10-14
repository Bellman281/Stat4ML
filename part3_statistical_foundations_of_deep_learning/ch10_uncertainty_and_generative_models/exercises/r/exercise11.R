# Chapter 10 exercise -- the conformal coverage quantile (Proof tier)
# level: proof
# HOMEWORK: ch10_text.tex Section 1.  Rscript exercise11.R

conformal_q <- function(cal_scores, alpha) {
  # TODO: k-th smallest score, k = ceiling((n+1)(1-alpha)); if k > n return Inf
  stop("TODO: conformal_q")
}
empirical_coverage <- function(test_scores, q) {
  # TODO: mean(test_scores <= q)
  stop("TODO: empirical_coverage")
}
guarantee_holds <- function(cov, alpha) {
  # TODO: cov >= 1 - alpha - 1e-9
  stop("TODO: guarantee_holds")
}

main <- function() {
  cal <- c(0.2, 0.4, 0.6, 0.8, 1.0)
  q <- conformal_q(cal, 0.2)
  cat("conformal_q       :", q, "\n")
  cov <- empirical_coverage(c(0.5, 0.9, 1.5, 0.1, 0.7), q)
  cat("empirical_coverage:", cov, "\n")
  cat("guarantee_holds   :", guarantee_holds(cov, 0.2), "\n")
}
main()
