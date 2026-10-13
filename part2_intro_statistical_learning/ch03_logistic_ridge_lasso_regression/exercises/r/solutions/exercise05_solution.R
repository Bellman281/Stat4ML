# Chapter 3 -- reference solution (Research, R)
# level: research
l1_penalty <- function(beta, lam) lam * sum(abs(beta))
l2_penalty <- function(beta, lam) lam * sum(beta^2)
elastic_net_penalty <- function(beta, lam, alpha) lam * (alpha * sum(abs(beta)) + (1 - alpha) * sum(beta^2))
main <- function() {
  b <- c(1, -2, 3)
  cat("l1          :", l1_penalty(b, 1.0), "\n")
  cat("l2          :", l2_penalty(b, 1.0), "\n")
  cat("elastic net :", elastic_net_penalty(b, 1.0, 0.25), "\n")
}
main()
