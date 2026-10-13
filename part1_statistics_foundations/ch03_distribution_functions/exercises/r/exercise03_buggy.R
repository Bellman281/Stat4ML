# Chapter 3 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (exponential_pdf, inverse_transform_exponential).

exponential_cdf <- function(x, rate) 1 - exp(-rate * x)
exponential_pdf <- function(x, rate) {
  # BUG: drops the leading factor of `rate`.
  exp(-rate * x)
}
inverse_transform_exponential <- function(u, rate) {
  # BUG: missing the minus sign; F^{-1}(u) = -log(1-u)/rate.
  log(1 - u) / rate
}
empirical_cdf <- function(data, x) mean(data <= x)

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("exponential_cdf(ln2)", exponential_cdf(log(2), 1.0), 0.5)
  check("exponential_pdf(0)", exponential_pdf(0.0, 1.0), 1.0)
  check("exponential_pdf(1,rate2)", exponential_pdf(1.0, 2.0), 2 * exp(-2))
  check("inverse_transform(0.5)", inverse_transform_exponential(0.5, 1.0), log(2))
  check("empirical_cdf(2.5)", empirical_cdf(c(1, 2, 3, 4), 2.5), 0.5)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
