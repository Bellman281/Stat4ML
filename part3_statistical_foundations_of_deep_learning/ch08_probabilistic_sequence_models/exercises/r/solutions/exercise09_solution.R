# Chapter 8 -- reference solution (Proof, R)
# level: proof
chain_rule_prob <- function(conditionals) prod(conditionals)
avg_cross_entropy <- function(conditionals) -mean(log(conditionals))
perplexity <- function(avg_ce) exp(avg_ce)
main <- function() {
  c <- c(0.5, 0.5, 0.25)
  cat("chain_rule_prob :", chain_rule_prob(c), "\n")
  ace <- avg_cross_entropy(c)
  cat("avg_cross_entropy:", ace, "\n")
  cat("perplexity       :", perplexity(ace), "\n")
  cat("joint^(-1/n)     :", chain_rule_prob(c)^(-1 / length(c)), "\n")
}
main()
