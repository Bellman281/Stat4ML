# Chapter 4 exercise -- the ELBO and the VAE's KL term (Research tier)
# level: research
# HOMEWORK: ch04_text.tex Section 2.  Rscript exercise06.R

gaussian_kl <- function(mu, sigma2) {
  # TODO: 0.5 * (sigma2 + mu^2 - 1 - log(sigma2))
  stop("TODO: gaussian_kl")
}
mc_expectation <- function(samples) {
  # TODO: mean(samples)
  stop("TODO: mc_expectation")
}
elbo <- function(recon_loglik, mu, sigma2) {
  # TODO: recon_loglik - gaussian_kl(mu, sigma2)
  stop("TODO: elbo")
}

main <- function() {
  cat("gaussian_kl(0,1)  :", gaussian_kl(0.0, 1.0), "\n")
  cat("gaussian_kl(1,1)  :", gaussian_kl(1.0, 1.0), "\n")
  r <- mc_expectation(c(-2.0, -1.0, -3.0))
  cat("mc_expectation    :", r, "\n")
  cat("elbo              :", elbo(r, 1.0, 1.0), "\n")
}
main()
