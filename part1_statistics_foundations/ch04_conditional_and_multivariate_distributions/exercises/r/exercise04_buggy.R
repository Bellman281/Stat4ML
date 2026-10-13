# Chapter 4 -- RUSTLINGS-STYLE EXERCISE (R, Core tier)
# level: core
# Two deliberate bugs (conditional_y_prob, joint_covariance).

JOINT <- list(x = c(0, 0, 1, 1), y = c(0, 1, 0, 1), p = c(0.3, 0.2, 0.1, 0.4))

marginal_x_prob <- function(joint, x0) sum(joint$p[joint$x == x0])
marginal_y_prob <- function(joint, y0) sum(joint$p[joint$y == y0])
conditional_y_prob <- function(joint, y0, x0) {
  # BUG: conditioning on X=x0 divides by P(X=x0), not P(Y=y0).
  num <- sum(joint$p[joint$x == x0 & joint$y == y0])
  num / marginal_y_prob(joint, y0)
}
joint_covariance <- function(joint) {
  # BUG: covariance subtracts E[X]E[Y]; this returns E[XY] alone.
  sum(joint$x * joint$y * joint$p)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("marginal_x_prob(0)", marginal_x_prob(JOINT, 0), 0.5)
  check("conditional P(Y=1|X=0)", conditional_y_prob(JOINT, 1, 0), 0.4)
  check("conditional P(Y=1|X=1)", conditional_y_prob(JOINT, 1, 1), 0.8)
  check("joint_covariance", joint_covariance(JOINT), 0.1)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
