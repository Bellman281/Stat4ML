# Chapter 5 exercise -- the decomposition and Gibbs' inequality (Proof tier)
# level: proof
# HOMEWORK: ch05_text.tex Section 1.  Rscript exercise06.R

.entropy <- function(p) -sum(p * log(p))
.cross_entropy <- function(p, q) -sum(p * log(q))
.kl <- function(p, q) sum(p * log(p / q))

identity_residual <- function(p, q) {
  # TODO: cross_entropy(p,q) - entropy(p) - kl(p,q)  (must be ~0)
  stop("TODO: identity_residual")
}
kl_is_nonneg <- function(p, q) {
  # TODO: TRUE iff KL(p||q) >= -1e-12
  stop("TODO: kl_is_nonneg")
}
log_bound_gap <- function(t) {
  # TODO: (t - 1) - log(t)
  stop("TODO: log_bound_gap")
}

main <- function() {
  p <- c(0.2, 0.3, 0.5); q <- c(0.3, 0.4, 0.3)
  cat("identity_residual:", identity_residual(p, q), "\n")
  cat("kl_is_nonneg     :", kl_is_nonneg(p, q), "\n")
  cat("log_bound_gap(2) :", log_bound_gap(2.0), "\n")
  cat("log_bound_gap(1) :", log_bound_gap(1.0), "\n")
}
main()
