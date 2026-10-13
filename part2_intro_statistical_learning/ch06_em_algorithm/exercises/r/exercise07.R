# Chapter 6 exercise -- The evidence lower bound (Proof tier)
# level: proof
# HOMEWORK: ch06_text.tex Section 2.  Rscript exercise07.R
# joint = c(p(x,z=1), p(x,z=2)); q over z; p = posterior.

log_evidence <- function(joint) {
  # TODO: log( sum(joint) )
  stop("TODO: log_evidence")
}
elbo <- function(q, joint) {
  # TODO: sum( q * (log(joint) - log(q)) )
  stop("TODO: elbo")
}
kl <- function(q, p) {
  # TODO: sum( q * log(q / p) )
  stop("TODO: kl")
}

main <- function() {
  joint <- c(0.2, 0.3); q <- c(0.5, 0.5); post <- c(0.4, 0.6)
  cat("log_evidence :", log_evidence(joint), "\n")
  cat("elbo         :", elbo(q, joint), "\n")
  cat("kl           :", kl(q, post), "\n")
  cat("elbo + kl    :", elbo(q, joint) + kl(q, post), "\n")
}
main()
