# Chapter 7 -- RUSTLINGS-STYLE EXERCISE (R, Proof tier)
# level: proof
# Two deliberate bugs (inertia, assign_step).

sq_dist <- function(a, b) sum((a - b)^2)

inertia <- function(data, labels, centroids) {
  # BUG: J sums the SQUARED distance; this takes a square root of the sum.
  sqrt(sum(sapply(seq_along(data), function(i) sq_dist(data[[i]], centroids[[labels[i]]]))))
}
assign_step <- function(data, centroids) {
  # BUG: assignment minimises distance -> which.min, not which.max.
  sapply(data, function(x) which.max(sapply(centroids, function(c) sq_dist(x, c))))
}
update_step <- function(data, labels, K) {
  lapply(seq_len(K), function(k) {
    members <- data[labels == k]
    if (length(members) == 0) return(c(0, 0))
    c(mean(sapply(members, function(p) p[1])), mean(sapply(members, function(p) p[2])))
  })
}

run_tests <- function() {
  failures <- c()
  check <- function(name, cond, detail = "") {
    cat(sprintf("[%s] %s%s\n", if (cond) "PASS" else "FAIL", name,
                if (nchar(detail)) paste0(": ", detail) else ""))
    if (!cond) failures[[length(failures) + 1]] <<- name
  }
  data <- list(c(0, 0), c(1, 0), c(10, 0), c(11, 0))
  cents <- list(c(0, 0), c(5, 0))

  labels <- assign_step(data, cents)
  check("assign_step", all(labels == c(1, 1, 2, 2)), paste("got", paste(labels, collapse = ",")))

  j_before <- inertia(data, labels, cents)
  check("inertia", abs(j_before - 62) < 1e-9, paste("got", format(j_before)))

  cents2 <- update_step(data, labels, 2)
  j_after <- inertia(data, labels, cents2)
  check("monotone (J_after <= J_before)", j_after <= j_before + 1e-9,
        sprintf("%s <= %s", format(j_after), format(j_before)))
  check("J_after value", abs(j_after - 1) < 1e-9, paste("got", format(j_after)))

  cat("\n")
  if (length(failures) > 0) { cat(sprintf("%d test(s) FAILED\n", length(failures))); quit(save = "no", status = 1) }
  cat("All tests passed!\n")
}
run_tests()
