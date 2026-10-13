# Chapter 5 exercise -- CLT via the MGF, and the delta method (Research tier)
# level: research
# HOMEWORK: implement each TODO using ch05_text.tex Sections 2-3. Rscript exercise07.R

mgf_standard_normal <- function(t) {
  # TODO: exp(t^2 / 2)
  stop("TODO: mgf_standard_normal")
}
clt_mgf_limit <- function(t, n) {
  # TODO: (1 + t^2 / (2*n))^n  -> exp(t^2/2)
  stop("TODO: clt_mgf_limit")
}
delta_method_variance <- function(gprime, sigma2) {
  # TODO: g'(theta)^2 * sigma^2
  stop("TODO: delta_method_variance")
}
delta_method_sd <- function(gprime, sigma2) {
  # TODO: |g'(theta)| * sqrt(sigma^2)
  stop("TODO: delta_method_sd")
}

main <- function() {
  cat("MGF N(0,1) at t=0.5 :", mgf_standard_normal(0.5), "\n")
  cat("CLT MGF limit t=2   :", clt_mgf_limit(2.0, 1e6), "\n")
  cat("delta variance      :", delta_method_variance(2.0, 3.0), "\n")
  cat("delta sd            :", delta_method_sd(2.0, 3.0), "\n")
}
main()
