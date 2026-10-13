# Chapter 5 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (projected_variance, top_eigenvalue_2x2).

matvec2 <- function(S, w) c(S[1,1]*w[1] + S[1,2]*w[2], S[2,1]*w[1] + S[2,2]*w[2])
projected_variance <- function(S, w) {
  # BUG: the variance is w . (S w), a scalar; this returns only the first
  # component of S w.
  matvec2(S, w)[1]
}
top_eigenvalue_2x2 <- function(S) {
  # BUG: the LARGEST eigenvalue uses the + root; this uses the - root.
  tr <- S[1,1] + S[2,2]; det <- S[1,1]*S[2,2] - S[1,2]*S[2,1]
  (tr - sqrt(tr^2 - 4*det)) / 2
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-5) {
    ok <- length(got) == length(expected) && all(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, paste(format(got), collapse=","), paste(format(expected), collapse=",")))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  I <- matrix(c(2, 0, 0, 1), 2, 2, byrow = TRUE)
  S <- matrix(c(2, 0.8, 0.8, 0.6), 2, 2, byrow = TRUE)
  check("matvec2", matvec2(I, c(1, 0)), c(2, 0))
  check("projected_variance", projected_variance(I, c(0.6, 0.8)), 1.36)
  check("top_eigenvalue_2x2", top_eigenvalue_2x2(S), 2.3627416998)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
