# Chapter 1 -- reference solution (Proof, R)
# level: proof
hoeffding_tail <- function(n, eps) 2 * exp(-2 * n * eps^2)
confidence_width <- function(n, delta) sqrt(log(2 / delta) / (2 * n))
finite_class_bound <- function(emp_risk, m, n, delta) {
  emp_risk + sqrt((log(m) + log(2 / delta)) / (2 * n))
}
main <- function() {
  cat("hoeffding_tail(100,0.1):", hoeffding_tail(100, 0.1), "\n")
  cat("confidence_width(200)  :", confidence_width(200, 0.05), "\n")
  cat("finite_class_bound     :", finite_class_bound(0.1, 1000, 500, 0.05), "\n")
}
main()
