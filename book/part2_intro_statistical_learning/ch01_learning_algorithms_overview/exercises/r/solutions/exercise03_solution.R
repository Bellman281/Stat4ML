# Reference solution for exercise03.R (Chapter 1, Part II, Exercise 3)

online_variance_update <- function(state, new_x) {
  n <- state$n + 1
  delta <- new_x - state$mean
  mean <- state$mean + delta / n
  delta2 <- new_x - mean
  m2 <- state$m2 + delta * delta2
  list(n = n, mean = mean, m2 = m2)
}

variance_from_state <- function(state) {
  if (state$n > 0) state$m2 / state$n else 0.0
}

pseudo_label_accuracy <- function(teacher_preds, true_labels) {
  sum(teacher_preds == true_labels) / length(true_labels)
}

semi_supervised_combined_accuracy <- function(labeled_acc, labeled_frac, pseudo_acc, unlabeled_frac) {
  labeled_frac * labeled_acc + unlabeled_frac * pseudo_acc
}

main <- function() {
  stream <- c(4.0, 6.0, 8.0, 2.0, 10.0)
  state <- list(n = 0, mean = 0.0, m2 = 0.0)
  for (x in stream) state <- online_variance_update(state, x)
  v <- variance_from_state(state)
  cat(sprintf("online variance = %g  (expect 8.0)\n", v))

  acc <- pseudo_label_accuracy(c(1, 0, 1, 1, 0), c(1, 0, 0, 1, 0))
  cat(sprintf("pseudo_label_accuracy = %g  (expect 0.8)\n", acc))

  combined <- semi_supervised_combined_accuracy(0.95, 0.1, acc, 0.9)
  cat(sprintf("semi_supervised_combined_accuracy = %.4f\n", combined))
}

main()
