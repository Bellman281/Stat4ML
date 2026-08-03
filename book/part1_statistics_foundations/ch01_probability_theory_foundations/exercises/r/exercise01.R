# Chapter 1 exercise -- Probability Theory Foundations
# Part I: Statistics Foundation for ML
#
# HOMEWORK: implement each TODO using only the definitions from
# ch01_text.tex (Kolmogorov's axioms, inclusion-exclusion, conditional
# probability, Bayes' theorem) and base R (set.seed/runif for simulation).
#
# Run with:  Rscript exercise01.R
# Reference solution: solutions/exercise01_solution.R

sample_space_two_coins <- function() {
  c("HH", "HT", "TH", "TT")
}

is_valid_probability_function <- function(p, sample_space, tol = 1e-9) {
  # p: named numeric vector, names = outcomes, values = probabilities.
  # TODO: return TRUE iff (1) names(p) is exactly sample_space (as a set),
  # (2) every value is >= 0, and (3) sum(p) is within `tol` of 1.
  stop("TODO: is_valid_probability_function")
}

complement_probability <- function(p_a) {
  # TODO: return P(A^c) = 1 - P(A)
  stop("TODO: complement_probability")
}

union_probability <- function(p_a, p_b, p_a_and_b) {
  # TODO: inclusion-exclusion: P(A u B) = P(A) + P(B) - P(A n B)
  stop("TODO: union_probability")
}

conditional_probability <- function(p_a_and_b, p_b) {
  # TODO: P(A | B) = P(A n B) / P(B)
  stop("TODO: conditional_probability")
}

bayes_theorem <- function(p_b_given_a, p_a, p_b) {
  # TODO: P(A | B) = P(B|A) * P(A) / P(B)
  stop("TODO: bayes_theorem")
}

bayes_theorem_partition <- function(p_b_given_ai, p_ai) {
  # TODO: full Bayes' theorem over a partition A_1..A_k.
  # p_b_given_ai and p_ai are equal-length numeric vectors.
  # Return posterior[i] = P(A_i|B) = p_b_given_ai[i]*p_ai[i] / sum(...)
  stop("TODO: bayes_theorem_partition")
}

simulate_coin_law_of_large_numbers <- function(p_heads, n_tosses, seed = 0) {
  # TODO: set.seed(seed), draw n_tosses values from runif(n_tosses), count
  # how many are < p_heads, return that count / n_tosses.
  stop("TODO: simulate_coin_law_of_large_numbers")
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
