# Chapter 8 exercise -- sequence probability and perplexity (Core tier)
# level: core
# HOMEWORK: ch08_text.tex Section 1.  Rscript exercise08.R

seq_logprob <- function(conditionals) {
  # TODO: sum(log(conditionals))
  stop("TODO: seq_logprob")
}
perplexity_from_logprob <- function(total_logprob, n) {
  # TODO: exp(-total_logprob / n)
  stop("TODO: perplexity_from_logprob")
}
ngram_prob <- function(count, ctx_count, V, alpha) {
  # TODO: (count + alpha) / (ctx_count + alpha * V)
  stop("TODO: ngram_prob")
}

main <- function() {
  c <- c(0.5, 0.5, 0.25)
  lp <- seq_logprob(c)
  cat("seq_logprob            :", lp, "\n")
  cat("perplexity_from_logprob:", perplexity_from_logprob(lp, length(c)), "\n")
  cat("ngram_prob             :", ngram_prob(2, 10, 5, 1.0), "\n")
}
main()
