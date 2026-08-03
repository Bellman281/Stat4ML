# Chapter 2 exercise -- Moments
# Part I: Statistics Foundation for ML
#
# HOMEWORK: implement each TODO using only ch02_text.tex and base R.
# Run with:  Rscript exercise02.R
# Reference solution: solutions/exercise02_solution.R

expected_value <- function(values, probs) {
  # TODO: E[X] = sum(values * probs)
  stop("TODO: expected_value")
}

variance <- function(values, probs) {
  # TODO: Var(X) = E[X^2] - (E[X])^2. Reuse expected_value().
  stop("TODO: variance")
}

covariance <- function(x_values, y_values, joint_probs) {
  # x_values, y_values, joint_probs are equal-length vectors describing
  # the joint distribution of (X,Y) row by row.
  # TODO: Cov(X,Y) = E[XY] - E[X]E[Y]
  stop("TODO: covariance")
}

correlation <- function(cov_xy, var_x, var_y) {
  # TODO: rho = Cov(X,Y) / (sqrt(var_x) * sqrt(var_y))
  stop("TODO: correlation")
}

normal_mgf_theoretical <- function(t, mu, sigma2) {
  # TODO: exp(mu*t + sigma2*t^2/2)
  stop("TODO: normal_mgf_theoretical")
}

normal_mgf_monte_carlo <- function(t, mu, sigma2, n, seed = 0) {
  # TODO: set.seed(seed), draw n samples from rnorm(n, mean=mu, sd=sqrt(sigma2)),
  # return mean(exp(t * samples)).
  stop("TODO: normal_mgf_monte_carlo")
}

main <- function() {
  xs <- c(0, 1, 2, 3)
  ps <- c(1 / 8, 3 / 8, 3 / 8, 1 / 8)  # Binomial(3, 0.5)
  mu <- expected_value(xs, ps)
  var <- variance(xs, ps)
  cat(sprintf("E[X] = %s, Var(X) = %s  (Binomial(3,0.5): expect mean 1.5, var 0.75)\n", mu, var))

  x_vals <- c(0, 0, 1, 1)
  y_vals <- c(0, 1, 0, 1)
  joint <- c(0.4, 0.1, 0.1, 0.4)  # positively associated
  cov <- covariance(x_vals, y_vals, joint)
  var_x <- variance(c(0, 1), c(0.5, 0.5))
  cat(sprintf("Cov(X,Y) = %s, corr = %s\n", cov, correlation(cov, var_x, var_x)))

  mu_n <- 2.0; sigma2_n <- 4.0; t <- 0.4
  theo <- normal_mgf_theoretical(t, mu_n, sigma2_n)
  mc <- normal_mgf_monte_carlo(t, mu_n, sigma2_n, 200000, seed = 7)
  cat(sprintf("Normal MGF at t=%.1f: theoretical=%.5f, Monte Carlo=%.5f\n", t, theo, mc))
}

main()
