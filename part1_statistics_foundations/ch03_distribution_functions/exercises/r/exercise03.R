# Chapter 3 exercise -- Distribution functions (Core)
# level: core
# HOMEWORK: ch03_text.tex Section 1. Base R only.  Rscript exercise03.R

exponential_cdf <- function(x, rate) {
  # TODO: 1 - exp(-rate * x)
  stop("TODO: exponential_cdf")
}
exponential_pdf <- function(x, rate) {
  # TODO: rate * exp(-rate * x)
  stop("TODO: exponential_pdf")
}
inverse_transform_exponential <- function(u, rate) {
  # TODO: -log(1 - u) / rate
  stop("TODO: inverse_transform_exponential")
}
empirical_cdf <- function(data, x) {
  # TODO: fraction of data <= x
  stop("TODO: empirical_cdf")
}

main <- function() {
  cat("F(ln2, rate=1) :", exponential_cdf(log(2), 1.0), "\n")
  cat("f(0, rate=1)   :", exponential_pdf(0.0, 1.0), "\n")
  cat("Finv(0.5)      :", inverse_transform_exponential(0.5, 1.0), "\n")
  cat("ecdf at 2.5    :", empirical_cdf(c(1, 2, 3, 4), 2.5), "\n")
}
main()
