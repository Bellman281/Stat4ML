# Chapter 10 exercise -- score matching and diffusion (Research tier)
# level: research
# HOMEWORK: ch10_text.tex Section 3.  Rscript exercise12.R

gaussian_score <- function(x, mu, sigma2) {
  # TODO: -(x - mu) / sigma2
  stop("TODO: gaussian_score")
}
denoising_target <- function(x_noisy, x_clean, sigma2) {
  # TODO: -(x_noisy - x_clean) / sigma2
  stop("TODO: denoising_target")
}
langevin_step <- function(x, score, step) {
  # TODO: x + step * score  (move uphill along the score)
  stop("TODO: langevin_step")
}

main <- function() {
  cat("gaussian_score  :", gaussian_score(3.0, 1.0, 2.0), "\n")
  cat("denoising_target:", denoising_target(3.0, 1.0, 2.0), "\n")
  cat("langevin_step   :", langevin_step(3.0, -1.0, 0.5), "\n")
}
main()
