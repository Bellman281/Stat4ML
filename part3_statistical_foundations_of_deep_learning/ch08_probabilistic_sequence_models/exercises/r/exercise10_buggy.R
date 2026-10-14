# Chapter 8 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (attention, pmi).

softmax_weights <- function(scores) {
  e <- exp(scores - max(scores))
  e / sum(e)
}
attention <- function(scores, values) {
  w <- softmax_weights(scores)
  # BUG: the output is the weighted sum sum(w * values); this forgets the values
  # and returns the weight total (always 1).
  sum(w)
}
pmi <- function(p_xy, p_x, p_y) {
  # BUG: PMI is log( p_xy / (p_x p_y) ); this inverts the ratio.
  log(p_x * p_y / p_xy)
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
  check("softmax_weights", softmax_weights(c(0.0, 0.0)), c(0.5, 0.5))
  check("attention", attention(c(0.0, 0.0), c(2.0, 4.0)), 3.0)
  check("attention_peaked", attention(c(100.0, 0.0), c(7.0, 1.0)), 7.0, tol = 1e-6)
  check("pmi", pmi(0.1, 0.2, 0.25), log(2.0))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
