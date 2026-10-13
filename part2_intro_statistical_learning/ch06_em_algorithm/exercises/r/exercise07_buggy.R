# Chapter 6 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (elbo, kl).

log_evidence <- function(joint) log(sum(joint))
elbo <- function(q, joint) {
  # BUG: the ELBO subtracts the entropy term log(q); this keeps only q*log(joint).
  sum(q * log(joint))
}
kl <- function(q, p) {
  # BUG: KL(q||p) uses log(q/p), not log(p/q).
  sum(q * log(p / q))
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  joint <- c(0.2, 0.3); q <- c(0.5, 0.5); post <- c(0.4, 0.6)
  check("log_evidence", log_evidence(joint), log(0.5))
  check("elbo", elbo(q, joint), 0.5 * log(0.4) + 0.5 * log(0.6))
  check("kl", kl(q, post), 0.5 * log(0.5 / 0.4) + 0.5 * log(0.5 / 0.6))
  check("identity", elbo(q, joint) + kl(q, post), log(0.5))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
