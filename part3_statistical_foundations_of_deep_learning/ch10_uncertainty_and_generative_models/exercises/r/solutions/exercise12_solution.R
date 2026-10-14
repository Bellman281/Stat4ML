# Chapter 10 -- reference solution (Research, R)
# level: research
gaussian_score <- function(x, mu, sigma2) -(x - mu) / sigma2
denoising_target <- function(x_noisy, x_clean, sigma2) -(x_noisy - x_clean) / sigma2
langevin_step <- function(x, score, step) x + step * score
main <- function() {
  cat("gaussian_score  :", gaussian_score(3.0, 1.0, 2.0), "\n")
  cat("denoising_target:", denoising_target(3.0, 1.0, 2.0), "\n")
  cat("langevin_step   :", langevin_step(3.0, -1.0, 0.5), "\n")
}
main()
