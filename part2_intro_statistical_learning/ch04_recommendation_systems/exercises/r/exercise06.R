# Chapter 4 exercise -- Funk SVD SGD step and biases (Research tier, R)
# level: research
# HOMEWORK: ch04_text.tex Section 3. Implement:
#   predict_bias : mu + b_u + b_i + p.q
#   sgd_update   : err = r - p.q ;  p <- p + lr*(err*q - lam*p),
#                  q <- q + lr*(err*p - lam*q)  (use OLD p);  return list(p_new,q_new,err)

predict_rating <- function(p, q) sum(p * q)

predict_bias <- function(mu, bu, bi, p, q) {
  # TODO: mu + b_u + b_i + p.q
  stop("TODO: predict_bias")
}
sgd_update <- function(p, q, r, lr, lam) {
  # TODO: one Funk-SVD SGD step; return list(p_new = ..., q_new = ..., err = ...)
  stop("TODO: sgd_update")
}

main <- function() {
  cat("predict_bias :", predict_bias(3.5, 0.2, -0.1, c(1, 0), c(2, 1)), "\n")
  out <- sgd_update(c(1, 0.5), c(0.5, 2), 4, 0.1, 0.05)
  cat("err          :", out$err, "\n")
  cat("p_new        :", out$p_new, "\n")
  cat("q_new        :", out$q_new, "\n")
}
main()
