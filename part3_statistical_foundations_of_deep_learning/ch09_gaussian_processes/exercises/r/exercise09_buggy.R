# Chapter 9 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (rbf_kernel, linear_kernel).

rbf_kernel <- function(x1, x2, length) {
  # BUG: the RBF kernel divides by 2*length^2, not length^2.
  exp(-(x1 - x2)^2 / (length^2))
}
kernel_vector <- function(x, xs, length) sapply(xs, function(xi) rbf_kernel(x, xi, length))
linear_kernel <- function(x1, x2) {
  # BUG: the linear kernel is the PRODUCT x1*x2, not the sum.
  x1 + x2
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
  check("rbf_same", rbf_kernel(0.0, 0.0, 1.0), 1.0)
  check("rbf_diff", rbf_kernel(0.0, 1.0, 1.0), exp(-0.5))
  check("kernel_vector", kernel_vector(0.0, c(0.0, 1.0, 2.0), 1.0), c(1.0, exp(-0.5), exp(-2.0)))
  check("linear_kernel", linear_kernel(2.0, 3.0), 6.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
