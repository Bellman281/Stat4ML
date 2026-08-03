# Chapter 0 exercise 1 -- Matrix Algebra Review: core operations
# Part I: Statistics Foundation for ML
#
# HOMEWORK: implement each TODO using only ch00_text.tex Sections 1-4
# (matrix multiplication, determinants, the inverse, transpose).
# Represent 2x2 matrices as R matrix() objects, but implement the
# operations yourself -- do not just call %*%, t(), det(), or solve().
#
# Run with:  Rscript exercise01.R
# Reference solution: solutions/exercise01_solution.R

matmul <- function(A, B) {
  # TODO: return A %*% B without using the built-in %*% operator.
  stop("TODO: matmul")
}

transpose <- function(A) {
  # TODO: return t(A) without using the built-in t() function.
  stop("TODO: transpose")
}

det2x2 <- function(A) {
  # TODO: det(A) = ad - bc for A = [[a,b],[c,d]].
  stop("TODO: det2x2")
}

inverse2x2 <- function(A) {
  # TODO: A^-1 = (1/det A) * [[d,-b],[-c,a]]. Assume det(A) != 0.
  stop("TODO: inverse2x2")
}

main <- function() {
  A <- matrix(c(1, 2, 3, 4), nrow = 2, byrow = TRUE)  # [[1,2],[3,4]]
  B <- matrix(c(5, 6, 7, 8), nrow = 2, byrow = TRUE)  # [[5,6],[7,8]]

  AB <- matmul(A, B)
  cat("AB =\n"); print(AB)

  lhs <- transpose(AB)
  rhs <- matmul(transpose(B), transpose(A))
  cat("(AB)^T =\n"); print(lhs)
  cat("B^T A^T =\n"); print(rhs)

  dA <- det2x2(A); dB <- det2x2(B); dAB <- det2x2(AB)
  cat(sprintf("det(A)*det(B) = %g, det(AB) = %g -- should match\n", dA * dB, dAB))

  invA <- inverse2x2(A)
  check <- matmul(A, invA)
  cat("A @ A^-1 =\n"); print(check)
}

main()
