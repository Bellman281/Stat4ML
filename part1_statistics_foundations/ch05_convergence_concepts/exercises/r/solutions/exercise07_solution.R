# Chapter 5 -- reference solution (Research, R)
# level: research
mgf_standard_normal <- function(t) exp(t * t / 2)
clt_mgf_limit <- function(t, n) (1 + t * t / (2 * n))^n
delta_method_variance <- function(gprime, sigma2) gprime^2 * sigma2
delta_method_sd <- function(gprime, sigma2) abs(gprime) * sqrt(sigma2)

main <- function() {
  cat("MGF N(0,1) at t=0.5 :", mgf_standard_normal(0.5), "\n")
  cat("CLT MGF limit t=2   :", clt_mgf_limit(2.0, 1e6), "\n")
  cat("delta variance      :", delta_method_variance(2.0, 3.0), "\n")
  cat("delta sd            :", delta_method_sd(2.0, 3.0), "\n")
}
main()
