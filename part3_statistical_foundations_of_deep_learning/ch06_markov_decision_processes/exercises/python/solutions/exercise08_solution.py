"""Chapter 6 -- reference solution (Research)."""
# level: research


def mc_update(v, G, alpha):
    return v + alpha * (G - v)


def td_error(r, gamma, v_next, v):
    return r + gamma * v_next - v


def td_update(v, r, gamma, v_next, alpha):
    return v + alpha * td_error(r, gamma, v_next, v)


def main():
    print("mc_update :", mc_update(0.5, 1.0, 0.1))
    print("td_error  :", td_error(0.0, 0.9, 1.0, 0.5))
    print("td_update :", td_update(0.5, 0.0, 0.9, 1.0, 0.1))


if __name__ == "__main__":
    main()
