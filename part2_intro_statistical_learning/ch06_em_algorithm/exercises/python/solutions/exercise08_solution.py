"""Chapter 6 -- reference solution (Research)."""
# level: research
def hard_assignment(resp):
    best = 0
    for i in range(len(resp)):
        if resp[i] > resp[best]:
            best = i
    return best


def responsibility_based_weight(resp_column):
    return sum(resp_column) / len(resp_column)


def em_lower_bound_gap(ll_before, ll_after):
    return ll_after - ll_before


def main():
    print("hard_assignment :", hard_assignment([0.2, 0.7, 0.1]))
    print("weight          :", responsibility_based_weight([0.5, 0.5, 1.0, 0.0]))
    print("em gap          :", em_lower_bound_gap(1.0, 1.5))


if __name__ == "__main__":
    main()
