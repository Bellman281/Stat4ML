# Chapter 3 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (harmonic_partial, rm_valid).

harmonic_partial <- function(T) {
  # BUG: the sum runs t = 1..T inclusive; 1:(T-1) drops the last term.
  sum(1 / seq_len(T - 1))
}
basel_partial <- function(T) sum(1 / seq_len(T)^2)
rm_valid <- function(p) {
  # BUG: the squared sum converges only for p > 1/2 (strict); p = 1/2 diverges.
  (p >= 0.5) && (p <= 1.0)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- if (is.logical(expected)) identical(got, expected) else isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("harmonic_partial", harmonic_partial(4), 1 + 1/2 + 1/3 + 1/4)
  check("basel_partial", basel_partial(2), 1 + 1/4)
  check("rm_valid_1.0", rm_valid(1.0), TRUE)
  check("rm_valid_0.75", rm_valid(0.75), TRUE)
  check("rm_valid_0.5", rm_valid(0.5), FALSE)
  check("rm_valid_0.4", rm_valid(0.4), FALSE)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
