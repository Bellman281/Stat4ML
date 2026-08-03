# Chapter 1 -- RUSTLINGS-STYLE EXERCISE (R edition)
# Part I: Statistics Foundation for ML
#
# Every function below is fully implemented -- but FIVE contain a
# deliberate bug that violates something from ch01_text.tex. Find and fix
# each one so every check in run_tests() passes. Do not edit run_tests().
#
# Run with:  Rscript exercise01_buggy.R

sample_space_two_coins <- function() {
  c("HH", "HT", "TH", "TT")
}

is_valid_probability_function <- function(p, sample_space, tol = 1e-9) {
  # BUG: only checks the sum -- forgets non-negativity (Axiom 1) and
  # forgets to check that names(p) matches sample_space.
  abs(sum(p) - 1.0) < tol
}

complement_probability <- function(p_a) {
  # BUG: returns P(A) instead of 1 - P(A).
  p_a
}

union_probability <- function(p_a, p_b, p_a_and_b) {
  # BUG: forgets to subtract the intersection (inclusion-exclusion).
  p_a + p_b
}

conditional_probability <- function(p_a_and_b, p_b) {
  # Correct.
  p_a_and_b / p_b
}

bayes_theorem <- function(p_b_given_a, p_a, p_b) {
  # BUG: forgets to divide by P(B).
  p_b_given_a * p_a
}

bayes_theorem_partition <- function(p_b_given_ai, p_ai) {
  # Correct.
  denom <- sum(p_b_given_ai * p_ai)
  (p_b_given_ai * p_ai) / denom
}

simulate_coin_law_of_large_numbers <- function(p_heads, n_tosses, seed = 0) {
  # BUG: ignores p_heads and always thresholds at 0.5.
  set.seed(seed)
  draws <- runif(n_tosses)
  sum(draws < 0.5) / n_tosses
}

# ---------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# ---------------------------------------------------------------------------
run_tests <- function() {
  failures <- c()
  check <- function(name, got, expected, tol = 1e-9) {
    ok <- if (is.numeric(got) && is.numeric(expected)) abs(got - expected) < tol else isTRUE(all(got == expected))
    status <- if (ok) "PASS" else "FAIL"
    cat(sprintf("[%s] %s: got=%s expected=%s\n", status, name,
                paste(got, collapse = ","), paste(expected, collapse = ",")))
    if (!ok) failures <<- c(failures, name)
  }

  ss <- sample_space_two_coins()
  check("sample_space_two_coins", ss, c("HH", "HT", "TH", "TT"))

  fair <- setNames(rep(0.25, 4), ss)
  invalid <- setNames(c(0.5, -0.1, 0.3, 0.3), ss)  # negative prob!
  check("is_valid_probability_function(fair)", is_valid_probability_function(fair, ss), TRUE)
  check("is_valid_probability_function(invalid, has negative prob)",
        is_valid_probability_function(invalid, ss), FALSE)

  check("complement_probability(0.3)", complement_probability(0.3), 0.7)
  check("union_probability(0.5, 0.4, 0.2)", union_probability(0.5, 0.4, 0.2), 0.7)
  check("conditional_probability(0.2, 0.4)", conditional_probability(0.2, 0.4), 0.5)
  check("bayes_theorem", bayes_theorem(0.4, 0.5, 0.4), 0.5)

  post <- bayes_theorem_partition(c(0.9, 0.2), c(0.01, 0.99))
  expected_denom <- 0.9 * 0.01 + 0.2 * 0.99
  check("bayes_theorem_partition[1]", round(post[1], 6), round(0.9 * 0.01 / expected_denom, 6))

  freq <- simulate_coin_law_of_large_numbers(0.2, 200000, seed = 42)
  check("simulate_coin_law_of_large_numbers(p=0.2) converges near 0.2",
        round(freq, 1), 0.2, tol = 0.05)

  cat("\n")
  if (length(failures) > 0) {
    cat(sprintf("%d test(s) FAILED: %s\n", length(failures), paste(failures, collapse = ", ")))
    quit(status = 1)
  }
  cat("All tests passed!\n")
}

run_tests()
