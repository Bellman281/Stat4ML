# Chapter 3 -- reference solution (Core, R)
# level: core
sigmoid <- function(z) 1 / (1 + exp(-z))
logistic_proba <- function(w, x) sigmoid(sum(w * x))
cross_entropy <- function(y, p) -(y * log(p) + (1 - y) * log(1 - p))
classify <- function(p, threshold = 0.5) if (p >= threshold) 1 else 0
main <- function() {
  cat("sigmoid(0)        :", sigmoid(0.0), "\n")
  cat("proba([0,1,1],.)  :", logistic_proba(c(0, 1, 1), c(1, 2, -2)), "\n")
  cat("cross_entropy     :", cross_entropy(1, 0.5), "\n")
  cat("classify(0.7)     :", classify(0.7), "\n")
}
main()
