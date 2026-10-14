# Chapter 5 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (perplexity, mutual_information).

perplexity <- function(cross_entropy_nats) {
  # BUG: perplexity is exp(cross-entropy), not log of it.
  log(cross_entropy_nats)
}
joint_entropy <- function(joint) {
  p <- joint[joint > 0]
  -sum(p * log(p))
}
mutual_information <- function(joint) {
  px <- rowSums(joint); py <- colSums(joint)
  mi <- 0
  for (i in seq_len(nrow(joint))) for (j in seq_len(ncol(joint))) {
    pxy <- joint[i, j]
    if (pxy > 0) {
      # BUG: MI uses log( p(x,y) / (p(x) p(y)) ); this inverts the ratio.
      mi <- mi + pxy * log(px[i] * py[j] / pxy)
    }
  }
  mi
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  corr <- matrix(c(0.5, 0.0, 0.0, 0.5), nrow = 2, byrow = TRUE)
  indep <- matrix(c(0.25, 0.25, 0.25, 0.25), nrow = 2, byrow = TRUE)
  check("perplexity", perplexity(log(5)), 5.0)
  check("joint_entropy", joint_entropy(corr), log(2))
  check("MI_correlated", mutual_information(corr), log(2))
  check("MI_independent", mutual_information(indep), 0.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
