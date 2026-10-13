# Chapter 6 exercise -- The E and M steps (Core)
# level: core
# HOMEWORK: ch06_text.tex Section 1.  Rscript exercise06.R  (k is 1-based)

gaussian_pdf <- function(x, mu, s2) {
  # TODO: exp(-(x-mu)^2 / (2*s2)) / sqrt(2*pi*s2)
  stop("TODO: gaussian_pdf")
}
responsibility <- function(x, pis, mus, s2s, k) {
  # TODO: pis[k]*N_k / sum_j pis[j]*N_j
  stop("TODO: responsibility")
}
weighted_mean <- function(xs, resps) {
  # TODO: sum(resps*xs) / sum(resps)
  stop("TODO: weighted_mean")
}

main <- function() {
  cat("gaussian_pdf(0,0,1) :", gaussian_pdf(0, 0, 1), "\n")
  cat("responsibility      :", responsibility(0, c(0.5, 0.5), c(-1, 1), c(1, 1), 1), "\n")
  cat("weighted_mean       :", weighted_mean(c(1, 2, 3), c(1, 1, 0)), "\n")
}
main()
