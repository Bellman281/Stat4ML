# Chapter 4 -- RUSTLINGS-STYLE EXERCISE (R, Research tier)
# level: research
# Funk SVD SGD step + bias prediction (ch04_text.tex Section 3).
# Two deliberate bugs (predict_bias, sgd_update). Do not edit run_tests().

predict_rating <- function(p, q) sum(p * q)

predict_bias <- function(mu, bu, bi, p, q) {
  # BUG: the item bias b_i is dropped. Full model is mu + b_u + b_i + p.q.
  mu + bu + predict_rating(p, q)
}

sgd_update <- function(p, q, r, lr, lam) {
  # BUG: residual sign flipped. It must be err = r - p.q; reversed, the step
  # climbs the loss instead of descending it.
  err <- predict_rating(p, q) - r
  p_new <- p + lr * (err * q - lam * p)
  q_new <- q + lr * (err * p - lam * q)
  list(p_new = p_new, q_new = q_new, err = err)
}

run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- isTRUE(abs(got - expected) < tol)
    cat(sprintf("[%s] %s: got=%s expected=%s\n",
                if (ok) "PASS" else "FAIL", name, format(got), format(expected)))
    if (!ok) failures[[length(failures) + 1]] <<- name
  }
  check("predict_bias", predict_bias(3.5, 0.2, -0.1, c(1, 0), c(2, 1)), 5.6)
  p <- c(1, 0.5); q <- c(0.5, 2); r <- 4; lr <- 0.1; lam <- 0.05
  sq_before <- (r - predict_rating(p, q))^2
  out <- sgd_update(p, q, r, lr, lam)
  check("err", out$err, 2.5)
  check("p_new0", out$p_new[1], 1.12)
  check("p_new1", out$p_new[2], 0.9975)
  check("q_new0", out$q_new[1], 0.7475)
  check("q_new1", out$q_new[2], 2.115)
  sq_after <- (r - predict_rating(out$p_new, out$q_new))^2
  check("step_decreases_error", if (isTRUE(sq_after < sq_before)) 1 else 0, 1)
  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
