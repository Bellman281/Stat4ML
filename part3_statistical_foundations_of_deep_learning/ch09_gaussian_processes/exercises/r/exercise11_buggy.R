# Chapter 9 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Two deliberate bugs (relu, nngp_kernel).

relu <- function(z) {
  # BUG: ReLU is max(0, z) -- it zeros NEGATIVES; pmin zeros positives.
  pmin(0, z)
}
nn_features <- function(x, W, b) relu(W * x + b)
nngp_kernel <- function(feat1, feat2) {
  # BUG: the NNGP kernel AVERAGES over units (mean), not just sums.
  sum(feat1 * feat2)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(length(got) == length(expected) && all(abs(got - expected) < tol))
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name,
                paste(format(got), collapse = ","), paste(format(expected), collapse = ",")))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  W <- c(1.0, -1.0, 2.0); b <- c(0.0, 0.0, 0.0)
  check("relu_neg", relu(-2.0), 0.0)
  check("relu_pos", relu(3.0), 3.0)
  f1 <- nn_features(1.0, W, b)
  f2 <- nn_features(-1.0, W, b)
  check("nn_features", f1, c(1.0, 0.0, 2.0))
  check("nngp_same", nngp_kernel(f1, f1), (1.0 + 0.0 + 4.0) / 3)
  check("nngp_cross", nngp_kernel(f1, f2), 0.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
