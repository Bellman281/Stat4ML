# Chapter 1 exercise -- Hoeffding and the finite-class bound (Proof tier)
# level: proof
# HOMEWORK: ch01_text.tex Section 2.  Rscript exercise02.R

hoeffding_tail <- function(n, eps) {
  # TODO: 2 * exp(-2 * n * eps^2)
  stop("TODO: hoeffding_tail")
}
confidence_width <- function(n, delta) {
  # TODO: eps with hoeffding_tail(n, eps) = delta -> sqrt(log(2/delta)/(2n))
  stop("TODO: confidence_width")
}
finite_class_bound <- function(emp_risk, m, n, delta) {
  # TODO: emp_risk + sqrt((log(m) + log(2/delta)) / (2n))
  stop("TODO: finite_class_bound")
}

main <- function() {
  cat("hoeffding_tail(100,0.1):", hoeffding_tail(100, 0.1), "\n")
  cat("confidence_width(200)  :", confidence_width(200, 0.05), "\n")
  cat("finite_class_bound     :", finite_class_bound(0.1, 1000, 500, 0.05), "\n")
}
main()
