# Chapter 5 -- reference solution (Proof, R)
# level: proof
.entropy <- function(p) -sum(p * log(p))
.cross_entropy <- function(p, q) -sum(p * log(q))
.kl <- function(p, q) sum(p * log(p / q))

identity_residual <- function(p, q) .cross_entropy(p, q) - .entropy(p) - .kl(p, q)
kl_is_nonneg <- function(p, q) .kl(p, q) >= -1e-12
log_bound_gap <- function(t) (t - 1) - log(t)

main <- function() {
  p <- c(0.2, 0.3, 0.5); q <- c(0.3, 0.4, 0.3)
  cat("identity_residual:", identity_residual(p, q), "\n")
  cat("kl_is_nonneg     :", kl_is_nonneg(p, q), "\n")
  cat("log_bound_gap(2) :", log_bound_gap(2.0), "\n")
  cat("log_bound_gap(1) :", log_bound_gap(1.0), "\n")
}
main()
