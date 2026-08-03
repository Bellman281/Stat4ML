# Chapter 1 exercise 2 -- Random variables: PMF, CDF, and change of variables
# Part I: Statistics Foundation for ML
#
# HOMEWORK: implement each TODO using only ch01_text.tex Sections 5-6
# (random variables, CDFs, densities, and the change-of-variables /
# inverse-transform-sampling example with Y = -log(X)).
#
# Run with:  Rscript exercise02.R
# Reference solution: solutions/exercise02_solution.R

pmf_three_coins <- function(x) {
  # TODO: P(X = x) for X = number of heads in 3 fair coin tosses,
  # x in {0,1,2,3}: C(3,x) * (1/2)^3. See ch01_text.tex Section 5.
  stop("TODO: pmf_three_coins")
}

cdf_three_coins <- function(x) {
  # TODO: F_X(x) = P(X <= x), built from pmf_three_coins. Match the
  # table in ch01_text.tex Section 6.1 exactly.
  stop("TODO: cdf_three_coins")
}

inverse_transform_sample <- function(u) {
  # TODO: y = -log(u), Exponential(1)-distributed for u ~ Uniform(0,1)
  # (ch01_text.tex Section 8).
  stop("TODO: inverse_transform_sample")
}

exponential_pdf <- function(y) {
  # Provided for you -- not part of this exercise.
  if (y >= 0) exp(-y) else 0.0
}

main <- function() {
  total <- sum(sapply(0:3, pmf_three_coins))
  cat(sprintf("sum of pmf over x=0..3: %g  (should be 1.0)\n", total))

  cat(sprintf("F_X(2.5) = %g  (should be 7/8 = 0.875)\n", cdf_three_coins(2.5)))
  cat(sprintf("F_X(-1) = %g, F_X(3.5) = %g\n", cdf_three_coins(-1), cdf_three_coins(3.5)))

  set.seed(7)
  n <- 200000
  u <- pmax(runif(n), 1e-12)
  samples <- sapply(u, inverse_transform_sample)
  cat(sprintf("mean of %d inverse-transform samples: %.4f  (Exponential(1) mean is 1.0)\n", n, mean(samples)))
}

main()
