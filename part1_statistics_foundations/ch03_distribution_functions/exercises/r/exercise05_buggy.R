# Chapter 3 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (two_branch_pdf, jacobian_det_2d).

chi1_from_normal_pdf <- function(y) (1 / sqrt(2 * pi * y)) * exp(-y / 2)
two_branch_pdf <- function(fx_root1, fx_root2, gprime_abs) {
  # BUG: a non-monotone transform collects BOTH roots; this keeps one.
  fx_root1 / gprime_abs
}
jacobian_det_2d <- function(a, b, c, d) {
  # BUG: the determinant is a*d - b*c, not a*d + b*c.
  abs(a * d + b * c)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("chi1_from_normal_pdf(1)", chi1_from_normal_pdf(1.0),
        (1 / sqrt(2 * pi)) * exp(-0.5))
  check("two_branch_pdf", two_branch_pdf(0.2, 0.2, 4.0), 0.1)
  check("jacobian_det_2d", jacobian_det_2d(1, 2, 3, 4), 2.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
