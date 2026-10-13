# Chapter 8 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (relu, softmax).

sigmoid <- function(z) 1 / (1 + exp(-z))
relu <- function(z) {
  # BUG: ReLU is max(0, z) -- it zeros NEGATIVES; this zeros positives.
  min(0, z)
}
softmax <- function(zs) {
  # BUG: the stable softmax subtracts max(zs) before exp; without it this
  # overflows to Inf on large logits (ch08_text.tex Section 1).
  e <- exp(zs)
  e / sum(e)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(length(got) == length(expected) && all(abs(got - expected) < tol))
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name,
                paste(format(got), collapse = ","),
                paste(format(expected), collapse = ",")))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("sigmoid", sigmoid(0), 0.5)
  check("relu_neg", relu(-2), 0)
  check("relu_pos", relu(3), 3)
  check("softmax_uniform", softmax(c(1, 1, 1)), c(1/3, 1/3, 1/3))
  check("softmax_stable", softmax(c(1000, 1000)), c(0.5, 0.5))
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
