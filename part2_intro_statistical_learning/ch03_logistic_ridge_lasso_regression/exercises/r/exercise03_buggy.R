# Chapter 3 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (sigmoid, cross_entropy).

sigmoid <- function(z) {
  # BUG: the sigmoid is 1/(1+exp(-z)); the sign of z is flipped here.
  1 / (1 + exp(z))
}
logistic_proba <- function(w, x) sigmoid(sum(w * x))
cross_entropy <- function(y, p) {
  # BUG: cross-entropy keeps both terms; the (1-y)*log(1-p) half is dropped.
  -(y * log(p))
}
classify <- function(p, threshold = 0.5) if (p >= threshold) 1 else 0

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("sigmoid(0)", sigmoid(0.0), 0.5)
  check("sigmoid(2)", sigmoid(2.0), 1 / (1 + exp(-2)))
  check("logistic_proba", logistic_proba(c(0, 1, 1), c(1, 2, -2)), 0.5)
  check("cross_entropy(1,0.5)", cross_entropy(1, 0.5), log(2))
  check("cross_entropy(0,0.5)", cross_entropy(0, 0.5), log(2))
  check("classify(0.7)", classify(0.7), 1)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
