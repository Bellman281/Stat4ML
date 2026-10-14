# Chapter 1 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (sauer_bound, shatters).

sauer_bound <- function(n, d) {
  # BUG: Sauer-Shelah sums i from 0 to d; the i=0 term (choose(n,0)=1) is dropped.
  sum(choose(n, 1:d))
}
vc_bound_term <- function(d, n, delta) {
  sqrt((d * (log(2 * n / d) + 1) + log(4 / delta)) / n)
}
shatters <- function(patterns, n) {
  # BUG: shattering needs all 2^n DISTINCT patterns; this counts duplicates too.
  length(patterns) == 2^n
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- if (is.logical(expected)) identical(got, expected) else isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("sauer_bound", sauer_bound(5, 2), 16)
  check("vc_bound_term", vc_bound_term(10, 1000, 0.05),
        sqrt((10 * (log(200) + 1) + log(80)) / 1000))
  check("shatters_full", shatters(list(c(0, 0), c(0, 1), c(1, 0), c(1, 1)), 2), TRUE)
  check("shatters_dupes", shatters(list(c(0, 0), c(0, 0), c(1, 1), c(1, 1)), 2), FALSE)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
