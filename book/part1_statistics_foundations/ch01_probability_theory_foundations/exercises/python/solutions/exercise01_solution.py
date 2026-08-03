"""
Chapter 1 -- reference solution.
Same functions as exercise01.py, fully implemented. Also serves as the
"fixed" reference for exercise01_buggy.py: once you've patched every bug in
the buggy file, its behavior should match this one exactly.
"""
import random


def sample_space_two_coins():
    return ["HH", "HT", "TH", "TT"]


def is_valid_probability_function(p, sample_space, tol=1e-9):
    if set(p.keys()) != set(sample_space):
        return False
    if any(v < 0 for v in p.values()):
        return False
    return abs(sum(p.values()) - 1.0) < tol


def complement_probability(p_a):
    return 1.0 - p_a


def union_probability(p_a, p_b, p_a_and_b):
    return p_a + p_b - p_a_and_b


def conditional_probability(p_a_and_b, p_b):
    return p_a_and_b / p_b


def bayes_theorem(p_b_given_a, p_a, p_b):
    return p_b_given_a * p_a / p_b


def bayes_theorem_partition(p_b_given_ai, p_ai):
    denom = sum(pb * pa for pb, pa in zip(p_b_given_ai, p_ai))
    return [pb * pa / denom for pb, pa in zip(p_b_given_ai, p_ai)]


def simulate_coin_law_of_large_numbers(p_heads, n_tosses, seed=0):
    rng = random.Random(seed)
    heads = sum(1 for _ in range(n_tosses) if rng.random() < p_heads)
    return heads / n_tosses


def main():
    ss = sample_space_two_coins()
    fair = {o: 0.25 for o in ss}
    print("Two-coin sample space:", ss)
    print("Fair distribution valid?", is_valid_probability_function(fair, ss))

    p_a, p_b, p_ab = 0.5, 0.4, 0.2
    print("P(A^c) =", complement_probability(p_a))
    print("P(A u B) =", union_probability(p_a, p_b, p_ab))
    print("P(A | B) =", conditional_probability(p_ab, p_b))
    print("Bayes P(A|B) =", bayes_theorem(p_ab / p_a, p_a, p_b))

    for n in (10, 1_000, 100_000):
        freq = simulate_coin_law_of_large_numbers(0.5, n, seed=42)
        print(f"n={n:>7}: empirical P(heads) = {freq:.4f}")


if __name__ == "__main__":
    main()
