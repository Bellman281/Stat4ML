# Chapter 1 -- RUSTLINGS-STYLE EXERCISE (R edition), Exercise 3
# Part II: Introduction to Statistical Learning
#
# Three deliberate bugs are hiding below (in online_variance_update,
# variance_from_state, and pseudo_label_accuracy). Run this file, read
# the first failing check, fix ONLY that function, and re-run -- repeat
# until you see "All tests passed!". Do not edit run_tests().
#
# Run with:  Rscript exercise03_buggy.R

online_variance_update <- function(state, new_x) {
  # BUG: reuses `delta` (from the OLD mean) a second time instead of
  # computing `delta2` from the updated mean.
  n <- state$n + 1
  delta <- new_x - state$mean
  mean <- state$mean + delta / n
  m2 <- state$m2 + delta * delta
  list(n = n, mean = mean, m2 = m2)
}

variance_from_state <- function(state) {
  # BUG: uses the (n-1) sample-variance correction instead of
  # population variance m2/n.
  if (state$n > 1) state$m2 / (state$n - 1) else 0.0
}

pseudo_label_accuracy <- function(teacher_preds, true_labels) {
  # BUG: forgets to divide by the total count.
  sum(teacher_preds == true_labels)
}

semi_supervised_combined_accuracy <- function(labeled_acc, labeled_frac, pseudo_acc, unlabeled_frac) {
  # Correct.
  labeled_frac * labeled_acc + unlabeled_frac * pseudo_acc
}

# ---------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# ---------------------------------------------------------------------------
run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-6) {
    ok <- abs(got - expected) < tol
    status <- if (ok) "PASS" else "FAIL"
    cat(sprintf("[%s] %s: got=%s expected=%s\n", status, name, got, expected))
    if (!ok) failures <<- c(failures, name)
  }

  stream <- c(4.0, 6.0, 8.0, 2.0, 10.0)
  state <- list(n = 0, mean = 0.0, m2 = 0.0)
  for (x in stream) state <- online_variance_update(state, x)
  v <- variance_from_state(state)
  check("online variance", v, 8.0)

  acc <- pseudo_label_accuracy(c(1, 0, 1, 1, 0), c(1, 0, 0, 1, 0))
  check("pseudo_label_accuracy", acc, 0.8)

  combined <- semi_supervised_combined_accuracy(0.95, 0.1, acc, 0.9)
  check("semi_supervised_combined_accuracy", round(combined, 4), round(0.1 * 0.95 + 0.9 * 0.8, 4))

  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED: %s\n", length(failures), paste(failures, collapse = ", ")))
    quit(status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
