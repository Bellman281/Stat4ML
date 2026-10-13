# Chapter 3 -- reference solution (Proof, R)
# level: proof
numerical_pdf <- function(cdf, x, h = 1e-5) (cdf(x + h) - cdf(x - h)) / (2 * h)
change_of_variables <- function(fx, hprime) fx * abs(hprime)
square_uniform_pdf <- function(y) 1 / (2 * sqrt(y))

main <- function() {
  cdf <- function(x) 1 - exp(-x)
  cat("numerical pdf at 1 :", numerical_pdf(cdf, 1.0), "\n")
  cat("change_of_vars     :", change_of_variables(2.0, -3.0), "\n")
  cat("square_uniform(.25):", square_uniform_pdf(0.25), "\n")
}
main()
