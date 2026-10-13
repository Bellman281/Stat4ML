# Chapter 7 -- reference solution (Proof, R)
# level: proof
sq_dist <- function(a, b) sum((a - b)^2)

inertia <- function(data, labels, centroids) {
  sum(sapply(seq_along(data), function(i) sq_dist(data[[i]], centroids[[labels[i]]])))
}
assign_step <- function(data, centroids) {
  sapply(data, function(x) which.min(sapply(centroids, function(c) sq_dist(x, c))))
}
update_step <- function(data, labels, K) {
  lapply(seq_len(K), function(k) {
    members <- data[labels == k]
    if (length(members) == 0) return(c(0, 0))
    c(mean(sapply(members, function(p) p[1])), mean(sapply(members, function(p) p[2])))
  })
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
