# Chapter 5 exercise -- mutual information and perplexity (Research tier)
# level: research
# HOMEWORK: ch05_text.tex Sections 2-3.  Rscript exercise07.R
# joint is a matrix p(x,y) summing to 1.

perplexity <- function(cross_entropy_nats) {
  # TODO: exp(cross_entropy_nats)
  stop("TODO: perplexity")
}
joint_entropy <- function(joint) {
  # TODO: -sum over cells>0 of p log p
  stop("TODO: joint_entropy")
}
mutual_information <- function(joint) {
  # TODO: sum p(x,y) log( p(x,y) / (p(x) p(y)) ) over cells > 0
  stop("TODO: mutual_information")
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
