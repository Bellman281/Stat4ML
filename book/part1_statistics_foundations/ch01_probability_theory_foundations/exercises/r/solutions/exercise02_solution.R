# Reference solution for exercise02.R (Chapter 1, Exercise 2)

.choose3 <- function(x) {
  if (x %in% 0:3) c(1, 3, 3, 1)[x + 1] else 0
}

pmf_three_coins <- function(x) {
  .choose3(x) * (0.5^3)
}

cdf_three_coins <- function(x) {
  k <- floor(x)
  total <- 0
  for (i in 0:3) if (i <= k) total <- total + pmf_three_coins(i)
  total
}

inverse_transform_sample <- function(u) {
  -log(u)
}

exponential_pdf <- function(y) {
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
  samples <- inverse_transform_sample(u)
  cat(sprintf("mean of %d inverse-transform samples: %.4f  (Exponential(1) mean is 1.0)\n", n, mean(samples)))
}

main()
