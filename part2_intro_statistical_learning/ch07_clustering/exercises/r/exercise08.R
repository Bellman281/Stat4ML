# Chapter 7 exercise -- the objective and its two optimal steps (Proof tier)
# level: proof
# HOMEWORK: ch07_text.tex Section 2.  Rscript exercise08.R
# data = list of points c(x,y); labels = 1-based cluster indices;
# centroids = list of points. Build one Lloyd iteration from its pieces, then
# the test checks the chapter's claim: one iteration cannot RAISE J.

sq_dist <- function(a, b) sum((a - b)^2)  # provided

inertia <- function(data, labels, centroids) {
  # TODO: sum over i of sq_dist(data[[i]], centroids[[labels[i]]])
  stop("TODO: inertia")
}
assign_step <- function(data, centroids) {
  # TODO: for each point, the 1-based index of its nearest centroid
  stop("TODO: assign_step")
}
update_step <- function(data, labels, K) {
  # TODO: list of K centroids, each the mean of its assigned points
  stop("TODO: update_step")
}

main <- function() {
  data <- list(c(0, 0), c(1, 0), c(10, 0), c(11, 0))
  cents <- list(c(0, 0), c(5, 0))
  labels <- assign_step(data, cents)
  cat("labels   :", labels, "\n")
  cat("J before :", inertia(data, labels, cents), "\n")
  cents2 <- update_step(data, labels, 2)
  cat("J after  :", inertia(data, labels, cents2), "\n")
}
main()
