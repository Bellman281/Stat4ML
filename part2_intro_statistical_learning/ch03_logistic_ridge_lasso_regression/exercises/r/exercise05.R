# Chapter 3 exercise -- Penalties and the elastic net (Research tier)
# level: research
# HOMEWORK: ch03_text.tex Section 3.  Rscript exercise05.R

l1_penalty <- function(beta, lam) {
  # TODO: lam * sum(|b|)
  stop("TODO: l1_penalty")
}
l2_penalty <- function(beta, lam) {
  # TODO: lam * sum(b^2)
  stop("TODO: l2_penalty")
}
elastic_net_penalty <- function(beta, lam, alpha) {
  # TODO: lam * ( alpha*sum(|b|) + (1-alpha)*sum(b^2) )
  stop("TODO: elastic_net_penalty")
}

main <- function() {
  b <- c(1, -2, 3)
  cat("l1          :", l1_penalty(b, 1.0), "\n")
  cat("l2          :", l2_penalty(b, 1.0), "\n")
  cat("elastic net :", elastic_net_penalty(b, 1.0, 0.25), "\n")
}
main()
