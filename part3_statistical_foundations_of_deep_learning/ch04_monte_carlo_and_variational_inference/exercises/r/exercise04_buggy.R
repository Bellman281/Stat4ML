# Chapter 4 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (mc_variance, mc_standard_error).

mc_estimate <- function(fvals) mean(fvals)
mc_variance <- function(fvals) {
  # BUG: R's var() divides by n-1 (sample variance); the POPULATION variance
  # divides by n.
  var(fvals)
}
mc_standard_error <- function(fvals) {
  # BUG: the standard error is the SQUARE ROOT of variance/n; sqrt is missing.
  mc_variance(fvals) / length(fvals)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  f <- c(2, 4, 4, 4, 5, 5, 7, 9)
  check("mc_estimate", mc_estimate(f), 5.0)
  check("mc_variance", mc_variance(f), 4.0)
  check("mc_standard_error", mc_standard_error(f), sqrt(4.0 / 8))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
