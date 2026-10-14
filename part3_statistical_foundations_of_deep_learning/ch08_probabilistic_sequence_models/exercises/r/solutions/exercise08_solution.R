# Chapter 8 -- reference solution (Core, R)
# level: core
seq_logprob <- function(conditionals) sum(log(conditionals))
perplexity_from_logprob <- function(total_logprob, n) exp(-total_logprob / n)
ngram_prob <- function(count, ctx_count, V, alpha) (count + alpha) / (ctx_count + alpha * V)
main <- function() {
  c <- c(0.5, 0.5, 0.25)
  lp <- seq_logprob(c)
  cat("seq_logprob            :", lp, "\n")
  cat("perplexity_from_logprob:", perplexity_from_logprob(lp, length(c)), "\n")
  cat("ngram_prob             :", ngram_prob(2, 10, 5, 1.0), "\n")
}
main()
