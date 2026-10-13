# Chapter 6 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (gaussian_pdf, responsibility).

gaussian_pdf <- function(x, mu, s2) {
  # BUG: the 1/sqrt(2*pi*s2) normaliser is dropped.
  exp(-(x - mu)^2 / (2 * s2))
}
responsibility <- function(x, pis, mus, s2s, k) {
  # BUG: a responsibility is NORMALISED over components; this returns the
  # unnormalised pis[k]*N_k.
  pis[k] * gaussian_pdf(x, mus[k], s2s[k])
}
weighted_mean <- function(xs, resps) sum(resps * xs) / sum(resps)

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("gaussian_pdf(0,0,1)", gaussian_pdf(0, 0, 1), 1 / sqrt(2 * pi))
  check("responsibility", responsibility(0, c(0.5, 0.5), c(-1, 1), c(1, 1), 1), 0.5)
  check("weighted_mean", weighted_mean(c(1, 2, 3), c(1, 1, 0)), 1.5)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
