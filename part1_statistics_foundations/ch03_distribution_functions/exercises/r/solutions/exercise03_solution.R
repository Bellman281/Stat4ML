# Chapter 3 -- reference solution (Core, R)
# level: core
exponential_cdf <- function(x, rate) 1 - exp(-rate * x)
exponential_pdf <- function(x, rate) rate * exp(-rate * x)
inverse_transform_exponential <- function(u, rate) -log(1 - u) / rate
empirical_cdf <- function(data, x) mean(data <= x)

main <- function() {
  cat("F(ln2, rate=1) :", exponential_cdf(log(2), 1.0), "\n")
  cat("f(0, rate=1)   :", exponential_pdf(0.0, 1.0), "\n")
  cat("Finv(0.5)      :", inverse_transform_exponential(0.5, 1.0), "\n")
  cat("ecdf at 2.5    :", empirical_cdf(c(1, 2, 3, 4), 2.5), "\n")
}
main()
