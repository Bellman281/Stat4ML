# Chapter 5 -- reference solution (Proof, R)
# level: proof
matvec2 <- function(S, w) c(S[1,1]*w[1] + S[1,2]*w[2], S[2,1]*w[1] + S[2,2]*w[2])
projected_variance <- function(S, w) sum(w * matvec2(S, w))
top_eigenvalue_2x2 <- function(S) {
  tr <- S[1,1] + S[2,2]; det <- S[1,1]*S[2,2] - S[1,2]*S[2,1]
  (tr + sqrt(tr^2 - 4*det)) / 2
}
main <- function() {
  S <- matrix(c(2, 0.8, 0.8, 0.6), 2, 2, byrow = TRUE)
  I <- matrix(c(2, 0, 0, 1), 2, 2, byrow = TRUE)
  cat("matvec2       :", matvec2(I, c(1, 0)), "\n")
  cat("proj variance :", projected_variance(I, c(0.6, 0.8)), "\n")
  cat("top eigenvalue:", top_eigenvalue_2x2(S), "\n")
}
main()
