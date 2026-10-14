# Chapter 9 exercise -- the NNGP kernel (Research tier)
# level: research
# HOMEWORK: ch09_text.tex Section 3.  Rscript exercise11.R
# W, b are vectors (one entry per hidden unit).

relu <- function(z) {
  # TODO: pmax(0, z)
  stop("TODO: relu")
}
nn_features <- function(x, W, b) {
  # TODO: relu(W * x + b)  (a vector of hidden activations)
  stop("TODO: nn_features")
}
nngp_kernel <- function(feat1, feat2) {
  # TODO: mean(feat1 * feat2)
  stop("TODO: nngp_kernel")
}

main <- function() {
  W <- c(1.0, -1.0, 2.0); b <- c(0.0, 0.0, 0.0)
  f1 <- nn_features(1.0, W, b)
  f2 <- nn_features(-1.0, W, b)
  cat("relu(-2), relu(3):", relu(-2.0), relu(3.0), "\n")
  cat("nn_features(1)   :", f1, "\n")
  cat("nngp k(1,1)      :", nngp_kernel(f1, f1), "\n")
  cat("nngp k(1,-1)     :", nngp_kernel(f1, f2), "\n")
}
main()
