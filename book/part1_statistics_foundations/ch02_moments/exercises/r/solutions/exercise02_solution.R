# Chapter 2 -- reference solution (R)

expected_value <- function(values, probs) {
  sum(values * probs)
}

variance <- function(values, probs) {
  mu <- expected_value(values, probs)
  ex2 <- expected_value(values^2, probs)
  ex2 - mu^2
}

covariance <- function(x_values, y_values, joint_probs) {
  ex <- sum(x_values * joint_probs)
  ey <- sum(y_values * joint_probs)
  exy <- sum(x_values * y_values * joint_probs)
  exy - ex * ey
}

correlation <- function(cov_xy, var_x, var_y) {
  cov_xy / (sqrt(var_x) * sqrt(var_y))
}

normal_mgf_theoretical <- function(t, mu, sigma2) {
  exp(mu * t + sigma2 * t^2 / 2)
}

normal_mgf_monte_carlo <- function(t, mu, sigma2, n, seed = 0) {
  set.seed(seed)
  samples <- rnorm(n, mean = mu, sd = sqrt(sigma2))
  mean(exp(t * samples))
}

main <- function() {
  xs <- c(0, 1, 2, 3)
  ps <- c(1 / 8, 3 / 8, 3 / 8, 1 / 8)
  mu <- expected_value(xs, ps)
  var <- variance(xs, ps)
  cat(sprintf("E[X] = %s, Var(X) = %s  (Binomial(3,0.5): expect mean 1.5, var 0.75)\n", mu, var))

  x_vals <- c(0, 0, 1, 1)
  y_vals <- c(0, 1, 0, 1)
  joint <- c(0.4, 0.1, 0.1, 0.4)
  cov <- covariance(x_vals, y_vals, joint)
  var_x <- variance(c(0, 1), c(0.5, 0.5))
  cat(sprintf("Cov(X,Y) = %s, corr = %s\n", cov, correlation(cov, var_x, var_x)))

  mu_n <- 2.0; sigma2_n <- 4.0; t <- 0.4
  theo <- normal_mgf_theoretical(t, mu_n, sigma2_n)
  mc <- normal_mgf_monte_carlo(t, mu_n, sigma2_n, 200000, seed = 7)
  cat(sprintf("Normal MGF at t=%.1f: theoretical=%.5f, Monte Carlo=%.5f\n", t, theo, mc))
}

main()
