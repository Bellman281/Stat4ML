# Reference solution for exercise03.R (Chapter 1, Exercise 3)

independence_check <- function(p_a, p_b, p_a_and_b, tol = 1e-9) {
  abs(p_a_and_b - p_a * p_b) < tol
}

intersection_with_complement <- function(p_a, p_b_and_a) {
  p_a - p_b_and_a
}

exponential_cdf <- function(y) {
  if (y >= 0) 1.0 - exp(-y) else 0.0
}

probability_integral_transform_mean <- function(n, seed = 0) {
  set.seed(seed)
  u <- pmax(runif(n), 1e-12)
  x <- -log(u)
  y <- sapply(x, exponential_cdf)
  mean(y)
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
