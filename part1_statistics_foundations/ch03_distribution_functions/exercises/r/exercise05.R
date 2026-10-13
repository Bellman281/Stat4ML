# Chapter 3 exercise -- Non-monotone transforms and the Jacobian (Research tier)
# level: research
# HOMEWORK: ch03_text.tex Section 3.  Rscript exercise05.R

chi1_from_normal_pdf <- function(y) {
  # TODO: (1/sqrt(2*pi*y)) * exp(-y/2)
  stop("TODO: chi1_from_normal_pdf")
}
two_branch_pdf <- function(fx_root1, fx_root2, gprime_abs) {
  # TODO: (f_X(x1) + f_X(x2)) / |g'|
  stop("TODO: two_branch_pdf")
}
jacobian_det_2d <- function(a, b, c, d) {
  # TODO: |a*d - b*c|
  stop("TODO: jacobian_det_2d")
}

main <- function() {
  cat("chi2_1 pdf at 1 :", chi1_from_normal_pdf(1.0), "\n")
  cat("two_branch      :", two_branch_pdf(0.2, 0.2, 4.0), "\n")
  cat("jacobian det    :", jacobian_det_2d(1, 2, 3, 4), "\n")
}
main()
