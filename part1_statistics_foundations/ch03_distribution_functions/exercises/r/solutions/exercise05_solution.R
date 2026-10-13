# Chapter 3 -- reference solution (Research, R)
# level: research
chi1_from_normal_pdf <- function(y) (1 / sqrt(2 * pi * y)) * exp(-y / 2)
two_branch_pdf <- function(fx_root1, fx_root2, gprime_abs) (fx_root1 + fx_root2) / gprime_abs
jacobian_det_2d <- function(a, b, c, d) abs(a * d - b * c)

main <- function() {
  cat("chi2_1 pdf at 1 :", chi1_from_normal_pdf(1.0), "\n")
  cat("two_branch      :", two_branch_pdf(0.2, 0.2, 4.0), "\n")
  cat("jacobian det    :", jacobian_det_2d(1, 2, 3, 4), "\n")
}
main()
