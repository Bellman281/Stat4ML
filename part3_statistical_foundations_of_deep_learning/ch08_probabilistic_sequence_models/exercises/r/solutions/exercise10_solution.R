# Chapter 8 -- reference solution (Research, R)
# level: research
softmax_weights <- function(scores) {
  e <- exp(scores - max(scores))
  e / sum(e)
}
attention <- function(scores, values) sum(softmax_weights(scores) * values)
pmi <- function(p_xy, p_x, p_y) log(p_xy / (p_x * p_y))
main <- function() {
  cat("softmax_weights :", softmax_weights(c(0.0, 0.0)), "\n")
  cat("attention       :", attention(c(0.0, 0.0), c(2.0, 4.0)), "\n")
  cat("pmi             :", pmi(0.1, 0.2, 0.25), "\n")
}
main()
