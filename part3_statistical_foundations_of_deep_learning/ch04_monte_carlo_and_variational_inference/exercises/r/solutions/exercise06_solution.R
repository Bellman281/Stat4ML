# Chapter 4 -- reference solution (Research, R)
# level: research
gaussian_kl <- function(mu, sigma2) 0.5 * (sigma2 + mu^2 - 1 - log(sigma2))
mc_expectation <- function(samples) mean(samples)
elbo <- function(recon_loglik, mu, sigma2) recon_loglik - gaussian_kl(mu, sigma2)
main <- function() {
  cat("gaussian_kl(0,1)  :", gaussian_kl(0.0, 1.0), "\n")
  cat("gaussian_kl(1,1)  :", gaussian_kl(1.0, 1.0), "\n")
  r <- mc_expectation(c(-2.0, -1.0, -3.0))
  cat("mc_expectation    :", r, "\n")
  cat("elbo              :", elbo(r, 1.0, 1.0), "\n")
}
main()
