# Chapter 4 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (between_var, total_variance).

group_mean <- function(means, weights) sum(weights * means)
within_var <- function(vars, weights) sum(weights * vars)
between_var <- function(means, weights) {
  # BUG: Var(E[X|Y]) = E[m^2] - (E[m])^2; the squared mean is not subtracted.
  sum(weights * means^2)
}
total_variance <- function(vars, means, weights) {
  # BUG: total variance is within + between; this returns within only.
  within_var(vars, weights)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  w <- c(0.5, 0.5); m <- c(0.0, 10.0); v <- c(1.0, 1.0)
  check("group_mean", group_mean(m, w), 5.0)
  check("within_var", within_var(v, w), 1.0)
  check("between_var", between_var(m, w), 25.0)
  check("total_variance", total_variance(v, m, w), 26.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
