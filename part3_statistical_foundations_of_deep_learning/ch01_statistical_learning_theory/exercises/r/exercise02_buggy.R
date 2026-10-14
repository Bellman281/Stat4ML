# Chapter 1 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (confidence_width, finite_class_bound).

hoeffding_tail <- function(n, eps) 2 * exp(-2 * n * eps^2)
confidence_width <- function(n, delta) {
  # BUG: inverting 2 exp(-2 n eps^2) = delta gives sqrt(log(2/delta)/(2n));
  # the factor 2 inside the log is missing here.
  sqrt(log(1 / delta) / (2 * n))
}
finite_class_bound <- function(emp_risk, m, n, delta) {
  # BUG: the capacity term grows with log|H| = log(m), not m itself.
  emp_risk + sqrt((m + log(2 / delta)) / (2 * n))
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("hoeffding_tail", hoeffding_tail(100, 0.1), 2 * exp(-2))
  check("confidence_width", confidence_width(200, 0.05), sqrt(log(2 / 0.05) / 400))
  check("finite_class_bound", finite_class_bound(0.1, 1000, 500, 0.05),
        0.1 + sqrt((log(1000) + log(2 / 0.05)) / 1000))
  w <- confidence_width(300, 0.1)
  check("width inverts tail", hoeffding_tail(300, w), 0.1)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
