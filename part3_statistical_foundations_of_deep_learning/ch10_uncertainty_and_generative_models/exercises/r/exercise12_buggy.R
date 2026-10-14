# Chapter 10 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (gaussian_score, langevin_step).

gaussian_score <- function(x, mu, sigma2) {
  # BUG: the score points TOWARD the mean: -(x - mu)/sigma2; the sign is flipped.
  (x - mu) / sigma2
}
denoising_target <- function(x_noisy, x_clean, sigma2) -(x_noisy - x_clean) / sigma2
langevin_step <- function(x, score, step) {
  # BUG: generation moves UPHILL along the score: x + step*score.
  x - step * score
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("gaussian_score", gaussian_score(3.0, 1.0, 2.0), -1.0)
  check("denoising_target", denoising_target(3.0, 1.0, 2.0), -1.0)
  check("langevin_step", langevin_step(3.0, -1.0, 0.5), 2.5)
  check("DSM target = score", denoising_target(3.0, 1.0, 2.0), gaussian_score(3.0, 1.0, 2.0))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
