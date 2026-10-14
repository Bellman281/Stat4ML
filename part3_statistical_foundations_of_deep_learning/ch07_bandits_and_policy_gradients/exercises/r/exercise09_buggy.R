# Chapter 7 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (advantage, expected_grad).

logit_score <- function(a, probs) {
  ind <- rep(0, length(probs)); ind[a] <- 1
  ind - probs
}

advantage <- function(R, baseline) {
  # BUG: the advantage is R - baseline, not baseline - R.
  baseline - R
}
grad_estimate <- function(R, b, a, probs) (R - b) * logit_score(a, probs)
expected_grad <- function(rewards, b, probs) {
  acc <- rep(0, length(probs))
  for (a in seq_along(probs)) {
    # BUG: each action's gradient is weighted by probs[a]; the weighting is missing.
    acc <- acc + grad_estimate(rewards[a], b, a, probs)
  }
  acc
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
  probs <- c(0.2, 0.5, 0.3); rewards <- c(1.0, 2.0, 3.0)
  check("advantage", advantage(3.0, 2.0), 1.0)
  check("grad_estimate", grad_estimate(3.0, 2.0, 2, probs), c(-0.2, 0.5, -0.3))
  g0 <- expected_grad(rewards, 0.0, probs)
  g5 <- expected_grad(rewards, 5.0, probs)
  check("baseline invariance", g0, g5)
  true_g <- rowSums(sapply(seq_along(probs),
                           function(a) probs[a] * rewards[a] * logit_score(a, probs)))
  check("equals true gradient", g0, true_g)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
