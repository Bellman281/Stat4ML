# Chapter 8 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (perplexity_from_logprob, ngram_prob).

seq_logprob <- function(conditionals) sum(log(conditionals))
perplexity_from_logprob <- function(total_logprob, n) {
  # BUG: perplexity is exp(-logprob/n); the minus sign is missing.
  exp(total_logprob / n)
}
ngram_prob <- function(count, ctx_count, V, alpha) {
  # BUG: add-alpha smoothing adds alpha*V to the denominator, not just alpha.
  (count + alpha) / (ctx_count + alpha)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  c <- c(0.5, 0.5, 0.25)
  lp <- seq_logprob(c)
  check("seq_logprob", lp, log(0.5) + log(0.5) + log(0.25))
  check("perplexity_from_logprob", perplexity_from_logprob(lp, 3), exp(-lp / 3))
  check("ngram_prob", ngram_prob(2, 10, 5, 1.0), 3.0 / 15.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
