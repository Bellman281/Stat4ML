# Chapter 5 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (clt_mgf_limit, delta_method_variance).

mgf_standard_normal <- function(t) exp(t * t / 2)
clt_mgf_limit <- function(t, n) {
  # BUG: the term is t SQUARED over 2n, i.e. (1 + t*t/(2n))^n.
  (1 + t / (2 * n))^n
}
delta_method_variance <- function(gprime, sigma2) {
  # BUG: the delta-method variance has g'(theta) SQUARED.
  gprime * sigma2
}
delta_method_sd <- function(gprime, sigma2) abs(gprime) * sqrt(sigma2)

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("mgf_standard_normal", mgf_standard_normal(0.5), exp(0.125))
  check("clt_mgf_limit -> exp(2)", clt_mgf_limit(2.0, 1e6), exp(2.0), tol = 1e-2)
  check("delta_method_variance", delta_method_variance(2.0, 3.0), 12.0)
  check("delta_method_sd", delta_method_sd(2.0, 3.0), sqrt(12.0))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
