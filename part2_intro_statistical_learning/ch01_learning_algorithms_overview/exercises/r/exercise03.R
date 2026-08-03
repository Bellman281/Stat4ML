# Chapter 1 exercise 3 -- Online variance (Welford's algorithm) and
# semi-supervised pseudo-label accuracy
# Part II: Introduction to Statistical Learning
#
# HOMEWORK: implement each TODO. ch01_text.tex Section 4 (Online
# Learning) gives the running-mean update; this exercise extends it to
# running VARIANCE via Welford's algorithm, and implements a toy version
# of the "teacher generates pseudo-labels" idea from Section 3.
#
# Run with:  Rscript exercise03.R
# Reference solution: solutions/exercise03_solution.R

online_variance_update <- function(state, new_x) {
  # TODO: state = list(n=, mean=, m2=). Welford's update:
  #   n' = n+1; delta = new_x - mean; mean' = mean + delta/n'
  #   delta2 = new_x - mean'; m2' = m2 + delta*delta2
  stop("TODO: online_variance_update")
}

variance_from_state <- function(state) {
  # TODO: population variance = m2 / n.
  stop("TODO: variance_from_state")
}

pseudo_label_accuracy <- function(teacher_preds, true_labels) {
  # TODO: fraction of teacher_preds matching true_labels.
  stop("TODO: pseudo_label_accuracy")
}

semi_supervised_combined_accuracy <- function(labeled_acc, labeled_frac, pseudo_acc, unlabeled_frac) {
  # Provided for you -- not part of this exercise.
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
