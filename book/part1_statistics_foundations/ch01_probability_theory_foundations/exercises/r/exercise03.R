# Chapter 1 exercise 3 -- Independence and the probability integral transform
# Part I: Statistics Foundation for ML
#
# HOMEWORK: implement each TODO using only ch01_text.tex Section 4
# (Independence, and the P(B n A^c) = P(B) - P(A n B) identity) and
# Section 8 (the probability integral transform).
#
# Run with:  Rscript exercise03.R
# Reference solution: solutions/exercise03_solution.R

independence_check <- function(p_a, p_b, p_a_and_b, tol = 1e-9) {
  # TODO: True iff P(A n B) = P(A) P(B) within `tol`.
  stop("TODO: independence_check")
}

intersection_with_complement <- function(p_a, p_b_and_a) {
  # TODO: P(A n B^c) = P(A) - P(A n B).
  stop("TODO: intersection_with_complement")
}

exponential_cdf <- function(y) {
  # TODO: F_X(y) = 1 - e^{-y} for y >= 0, else 0.
  stop("TODO: exponential_cdf")
}

probability_integral_transform_mean <- function(n, seed = 0) {
  # TODO: sample n values x_i ~ Exponential(1) via -log(u), apply
  # exponential_cdf to get y_i, return mean(y_i) (should be ~0.5).
  stop("TODO: probability_integral_transform_mean")
}

main <- function() {
  cat(sprintf("independent (0.5, 0.4, 0.2): %s  (expect TRUE)\n", independence_check(0.5, 0.4, 0.2)))
  cat(sprintf("independent (0.5, 0.4, 0.3): %s  (expect FALSE)\n", independence_check(0.5, 0.4, 0.3)))

  cat(sprintf("P(A n B^c), A=0.5,B=0.4,AnB=0.3: %g  (expect 0.2)\n", intersection_with_complement(0.5, 0.3)))

  cat(sprintf("exponential_cdf(0) = %g  (expect 0)\n", exponential_cdf(0)))
  cat(sprintf("exponential_cdf(1) = %.4f  (expect ~0.6321)\n", exponential_cdf(1)))

  m <- probability_integral_transform_mean(200000, seed = 7)
  cat(sprintf("probability_integral_transform_mean = %.4f  (Uniform(0,1) mean is 0.5)\n", m))
}

main()
