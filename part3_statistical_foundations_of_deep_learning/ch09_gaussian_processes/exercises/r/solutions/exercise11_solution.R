# Chapter 9 -- reference solution (Research, R)
# level: research
relu <- function(z) pmax(0, z)
nn_features <- function(x, W, b) relu(W * x + b)
nngp_kernel <- function(feat1, feat2) mean(feat1 * feat2)
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
