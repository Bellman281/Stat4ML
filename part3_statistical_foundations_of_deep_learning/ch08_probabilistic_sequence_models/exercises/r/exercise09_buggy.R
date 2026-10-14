# Chapter 8 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (avg_cross_entropy, perplexity).

chain_rule_prob <- function(conditionals) prod(conditionals)
avg_cross_entropy <- function(conditionals) {
  # BUG: cross-entropy is the NEGATIVE mean log-prob; the minus sign is missing.
  mean(log(conditionals))
}
perplexity <- function(avg_ce) {
  # BUG: perplexity EXPONENTIATES the cross-entropy; this forgets the exp.
  avg_ce
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
  check("chain_rule_prob", chain_rule_prob(c), 0.5 * 0.5 * 0.25)
  ace <- avg_cross_entropy(c)
  check("avg_cross_entropy", ace, -(log(0.5) + log(0.5) + log(0.25)) / 3)
  check("perplexity", perplexity(ace), exp(ace))
  check("perplexity == joint^(-1/n)", perplexity(avg_cross_entropy(c)),
        chain_rule_prob(c)^(-1 / 3))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
