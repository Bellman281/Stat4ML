# Chapter 6 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (mc_update, td_error).

mc_update <- function(v, G, alpha) {
  # BUG: the update moves TOWARD G: v + alpha*(G - v); this uses (G + v).
  v + alpha * (G + v)
}
td_error <- function(r, gamma, v_next, v) {
  # BUG: the next value is discounted by gamma; the factor is missing here.
  r + v_next - v
}
td_update <- function(v, r, gamma, v_next, alpha) v + alpha * td_error(r, gamma, v_next, v)

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("mc_update", mc_update(0.5, 1.0, 0.1), 0.55)
  check("td_error", td_error(0.0, 0.9, 1.0, 0.5), 0.4)
  check("td_update", td_update(0.5, 0.0, 0.9, 1.0, 0.1), 0.54)
  check("fixed point", td_update(2.0, 0.0, 1.0, 2.0, 0.3), 2.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
