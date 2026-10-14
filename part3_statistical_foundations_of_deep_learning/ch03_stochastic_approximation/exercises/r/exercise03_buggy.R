# Chapter 3 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (sgd_step, quad_grad).

sgd_step <- function(theta, grad, lr) {
  # BUG: SGD moves AGAINST the gradient; this moves with it.
  theta + lr * grad
}
inverse_time_lr <- function(t, a0) a0 / t
quad_grad <- function(theta, target) {
  # BUG: d/dtheta (theta-target)^2 = 2(theta-target); the factor 2 is missing.
  theta - target
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("sgd_step", sgd_step(5.0, 2.0, 0.1), 4.8)
  check("inverse_time_lr", inverse_time_lr(4, 0.5), 0.125)
  check("quad_grad", quad_grad(5.0, 3.0), 4.0)
  check("one_step", sgd_step(5.0, quad_grad(5.0, 3.0), 0.25), 4.0)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
