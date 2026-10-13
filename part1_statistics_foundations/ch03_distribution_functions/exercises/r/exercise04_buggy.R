# Chapter 3 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (numerical_pdf, change_of_variables).

numerical_pdf <- function(cdf, x, h = 1e-5) {
  # BUG: a centered difference divides by 2h, not h.
  (cdf(x + h) - cdf(x - h)) / h
}
change_of_variables <- function(fx, hprime) {
  # BUG: the factor is |h'(y)| (a density is non-negative); abs is dropped.
  fx * hprime
}
square_uniform_pdf <- function(y) 1 / (2 * sqrt(y))

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-4) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  cdf <- function(x) 1 - exp(-x)
  check("numerical_pdf ~ e^-1", numerical_pdf(cdf, 1.0), exp(-1.0))
  check("change_of_variables", change_of_variables(2.0, -3.0), 6.0)
  check("square_uniform_pdf", square_uniform_pdf(0.25), 1.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
