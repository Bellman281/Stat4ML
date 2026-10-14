# Chapter 10 -- reference solution (Proof, R)
# level: proof
conformal_q <- function(cal_scores, alpha) {
  n <- length(cal_scores)
  k <- ceiling((n + 1) * (1 - alpha))
  if (k > n) return(Inf)
  sort(cal_scores)[k]
}
empirical_coverage <- function(test_scores, q) mean(test_scores <= q)
guarantee_holds <- function(cov, alpha) cov >= 1 - alpha - 1e-9
main <- function() {
  cal <- c(0.2, 0.4, 0.6, 0.8, 1.0)
  q <- conformal_q(cal, 0.2)
  cat("conformal_q       :", q, "\n")
  cov <- empirical_coverage(c(0.5, 0.9, 1.5, 0.1, 0.7), q)
  cat("empirical_coverage:", cov, "\n")
  cat("guarantee_holds   :", guarantee_holds(cov, 0.2), "\n")
}
main()
