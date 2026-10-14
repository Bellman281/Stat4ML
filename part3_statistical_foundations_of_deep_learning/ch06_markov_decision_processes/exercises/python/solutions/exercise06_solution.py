"""Chapter 6 -- reference solution (Core)."""
# level: core


def discounted_return(rewards, gamma):
    return sum(gamma ** t * r for t, r in enumerate(rewards))


def q_backup(r, gamma, next_values, probs):
    return r + gamma * sum(p * v for p, v in zip(probs, next_values))


def greedy_action(q_values):
    return max(range(len(q_values)), key=lambda i: q_values[i])


def main():
    print("discounted_return :", discounted_return([1, 1, 1], 0.5))
    print("q_backup          :", q_backup(0.0, 0.9, [10.0, 0.0], [0.8, 0.2]))
    print("greedy_action     :", greedy_action([1.0, 5.0, 3.0]))


if __name__ == "__main__":
    main()
