# Chapter 6 -- reference solution (Proof, R)
# level: proof
log_evidence <- function(joint) log(sum(joint))
elbo <- function(q, joint) sum(q * (log(joint) - log(q)))
kl <- function(q, p) sum(q * log(q / p))
main <- function() {
  joint <- c(0.2, 0.3); q <- c(0.5, 0.5); post <- c(0.4, 0.6)
  cat("log_evidence :", log_evidence(joint), "\n")
  cat("elbo         :", elbo(q, joint), "\n")
  cat("kl           :", kl(q, post), "\n")
  cat("elbo + kl    :", elbo(q, joint) + kl(q, post), "\n")
}
main()
