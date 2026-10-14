# Chapter 8 exercise -- attention as kernel smoothing, and PMI (Research tier)
# level: research
# HOMEWORK: ch08_text.tex Sections 2-3.  Rscript exercise10.R

softmax_weights <- function(scores) {
  # TODO: softmax of the scores (weights summing to 1)
  stop("TODO: softmax_weights")
}
attention <- function(scores, values) {
  # TODO: sum(softmax_weights(scores) * values)
  stop("TODO: attention")
}
pmi <- function(p_xy, p_x, p_y) {
  # TODO: log( p_xy / (p_x * p_y) )
  stop("TODO: pmi")
}

main <- function() {
  cat("softmax_weights :", softmax_weights(c(0.0, 0.0)), "\n")
  cat("attention       :", attention(c(0.0, 0.0), c(2.0, 4.0)), "\n")
  cat("pmi             :", pmi(0.1, 0.2, 0.25), "\n")
}
main()
