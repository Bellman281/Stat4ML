# Chapter 1 -- reference solution (R)
# Same functions as exercise01.R, fully implemented.

sample_space_two_coins <- function() {
  c("HH", "HT", "TH", "TT")
}

is_valid_probability_function <- function(p, sample_space, tol = 1e-9) {
  if (!setequal(names(p), sample_space)) return(FALSE)
  if (any(p < 0)) return(FALSE)
  abs(sum(p) - 1.0) < tol
}

complement_probability <- function(p_a) {
  1.0 - p_a
}

union_probability <- function(p_a, p_b, p_a_and_b) {
  p_a + p_b - p_a_and_b
}

conditional_probability <- function(p_a_and_b, p_b) {
  p_a_and_b / p_b
}

bayes_theorem <- function(p_b_given_a, p_a, p_b) {
  p_b_given_a * p_a / p_b
}

bayes_theorem_partition <- function(p_b_given_ai, p_ai) {
  denom <- sum(p_b_given_ai * p_ai)
  (p_b_given_ai * p_ai) / denom
}

simulate_coin_law_of_large_numbers <- function(p_heads, n_tosses, seed = 0) {
  set.seed(seed)
  draws <- runif(n_tosses)
  sum(draws < p_heads) / n_tosses
}

main <- function() {
  ss <- sample_space_two_coins()
  fair <- setNames(rep(0.25, 4), ss)
  cat("Two-coin sample space:", ss, "\n")
  cat("Fair distribution valid?", is_valid_probability_function(fair, ss), "\n")

  p_a <- 0.5; p_b <- 0.4; p_ab <- 0.2
  cat("P(A^c) =", complement_probability(p_a), "\n")
  cat("P(A u B) =", union_probability(p_a, p_b, p_ab), "\n")
  cat("P(A | B) =", conditional_probability(p_ab, p_b), "\n")
  cat("Bayes P(A|B) =", bayes_theorem(p_ab / p_a, p_a, p_b), "\n")

  for (n in c(10, 1000, 100000)) {
    freq <- simulate_coin_law_of_large_numbers(0.5, n, seed = 42)
    cat(sprintf("n=%7d: empirical P(heads) = %.4f\n", n, freq))
  }
}

main()
