# Chapter 3 exercise -- Logistic regression (Core)
# level: core
# HOMEWORK: ch03_text.tex Section 1.  Rscript exercise03.R

sigmoid <- function(z) {
  # TODO: 1 / (1 + exp(-z))
  stop("TODO: sigmoid")
}
logistic_proba <- function(w, x) {
  # TODO: sigmoid(sum(w * x))   (x includes a leading 1 for the bias)
  stop("TODO: logistic_proba")
}
cross_entropy <- function(y, p) {
  # TODO: -( y*log(p) + (1-y)*log(1-p) )
  stop("TODO: cross_entropy")
}
classify <- function(p, threshold = 0.5) {
  # TODO: 1 if p >= threshold else 0
  stop("TODO: classify")
}

main <- function() {
  cat("sigmoid(0)        :", sigmoid(0.0), "\n")
  cat("proba([0,1,1],.)  :", logistic_proba(c(0, 1, 1), c(1, 2, -2)), "\n")
  cat("cross_entropy     :", cross_entropy(1, 0.5), "\n")
  cat("classify(0.7)     :", classify(0.7), "\n")
}
main()
