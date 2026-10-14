# Chapter 8 exercise -- chain rule and perplexity = cross-entropy (Proof tier)
# level: proof
# HOMEWORK: ch08_text.tex Section 1 (and Chapter 5).  Rscript exercise09.R

chain_rule_prob <- function(conditionals) {
  # TODO: product of the conditionals
  stop("TODO: chain_rule_prob")
}
avg_cross_entropy <- function(conditionals) {
  # TODO: -mean(log(conditionals))
  stop("TODO: avg_cross_entropy")
}
perplexity <- function(avg_ce) {
  # TODO: exp(avg_ce)
  stop("TODO: perplexity")
}

main <- function() {
  c <- c(0.5, 0.5, 0.25)
  cat("chain_rule_prob :", chain_rule_prob(c), "\n")
  ace <- avg_cross_entropy(c)
  cat("avg_cross_entropy:", ace, "\n")
  cat("perplexity       :", perplexity(ace), "\n")
  cat("joint^(-1/n)     :", chain_rule_prob(c)^(-1 / length(c)), "\n")
}
main()
