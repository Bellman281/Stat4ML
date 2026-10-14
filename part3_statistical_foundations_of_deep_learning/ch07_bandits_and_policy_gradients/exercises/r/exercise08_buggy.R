# Chapter 7 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (logit_score, pg_grad).

softmax <- function(logits) { e <- exp(logits - max(logits)); e / sum(e) }

logit_score <- function(a, probs) {
  # BUG: the score is e_a - p (indicator minus p); this drops the indicator.
  -probs
}
pg_grad <- function(R, a, probs) {
  # BUG: the REINFORCE estimate scales the score by the reward R.
  logit_score(a, probs)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(length(got) == length(expected) && all(abs(got - expected) < tol))
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name,
                paste(format(got), collapse = ","), paste(format(expected), collapse = ",")))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("logit_score", logit_score(2, c(0.2, 0.5, 0.3)), c(-0.2, 0.5, -0.3))
  check("pg_grad", pg_grad(2.0, 2, c(0.2, 0.5, 0.3)), c(-0.4, 1.0, -0.6))
  p <- softmax(c(0.0, 0.5, -0.5))
  mean <- rowSums(sapply(seq_along(p), function(a) p[a] * logit_score(a, p)))
  check("mean score is zero", mean, c(0, 0, 0))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
