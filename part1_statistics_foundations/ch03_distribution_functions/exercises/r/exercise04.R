# Chapter 3 exercise -- Change of variables (Proof tier)
# level: proof
# HOMEWORK: ch03_text.tex Section 2.  Rscript exercise04.R

numerical_pdf <- function(cdf, x, h = 1e-5) {
  # TODO: centered difference (cdf(x+h) - cdf(x-h)) / (2*h)
  stop("TODO: numerical_pdf")
}
change_of_variables <- function(fx, hprime) {
  # TODO: f_X(h(y)) * |h'(y)|
  stop("TODO: change_of_variables")
}
square_uniform_pdf <- function(y) {
  # TODO: 1 / (2*sqrt(y))  for Y = X^2, X ~ U(0,1)
  stop("TODO: square_uniform_pdf")
}

main <- function() {
  cdf <- function(x) 1 - exp(-x)
  cat("numerical pdf at 1 :", numerical_pdf(cdf, 1.0), "\n")
  cat("change_of_vars     :", change_of_variables(2.0, -3.0), "\n")
  cat("square_uniform(.25):", square_uniform_pdf(0.25), "\n")
}
main()
