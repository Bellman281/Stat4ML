# Chapter 4 -- reference solution (Research, R): Funk SVD SGD step and biases
# level: research
predict_rating <- function(p, q) sum(p * q)
predict_bias <- function(mu, bu, bi, p, q) mu + bu + bi + predict_rating(p, q)
sgd_update <- function(p, q, r, lr, lam) {
  err <- r - predict_rating(p, q)
  p_new <- p + lr * (err * q - lam * p)
  q_new <- q + lr * (err * p - lam * q)   # uses the OLD p
  list(p_new = p_new, q_new = q_new, err = err)
}
main <- function() {
  cat("predict_bias :", predict_bias(3.5, 0.2, -0.1, c(1, 0), c(2, 1)), "\n")
  out <- sgd_update(c(1, 0.5), c(0.5, 2), 4, 0.1, 0.05)
  cat("err          :", out$err, "\n")
  cat("p_new        :", out$p_new, "\n")
  cat("q_new        :", out$q_new, "\n")
}
main()
