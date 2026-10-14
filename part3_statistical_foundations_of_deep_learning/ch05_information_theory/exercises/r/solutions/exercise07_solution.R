# Chapter 5 -- reference solution (Research, R)
# level: research
perplexity <- function(cross_entropy_nats) exp(cross_entropy_nats)
joint_entropy <- function(joint) {
  p <- joint[joint > 0]
  -sum(p * log(p))
}
mutual_information <- function(joint) {
  px <- rowSums(joint); py <- colSums(joint)
  mi <- 0
  for (i in seq_len(nrow(joint))) for (j in seq_len(ncol(joint))) {
    pxy <- joint[i, j]
    if (pxy > 0) mi <- mi + pxy * log(pxy / (px[i] * py[j]))
  }
  mi
}
main <- function() {
  corr <- matrix(c(0.5, 0.0, 0.0, 0.5), nrow = 2, byrow = TRUE)
  indep <- matrix(c(0.25, 0.25, 0.25, 0.25), nrow = 2, byrow = TRUE)
  cat("perplexity(log 5)   :", perplexity(log(5)), "\n")
  cat("joint_entropy(corr) :", joint_entropy(corr), "\n")
  cat("MI(correlated)      :", mutual_information(corr), "\n")
  cat("MI(independent)     :", mutual_information(indep), "\n")
}
main()
