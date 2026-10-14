# Chapter 6 -- reference solution (Research, R)
# level: research
mc_update <- function(v, G, alpha) v + alpha * (G - v)
td_error <- function(r, gamma, v_next, v) r + gamma * v_next - v
td_update <- function(v, r, gamma, v_next, alpha) v + alpha * td_error(r, gamma, v_next, v)
main <- function() {
  cat("mc_update :", mc_update(0.5, 1.0, 0.1), "\n")
  cat("td_error  :", td_error(0.0, 0.9, 1.0, 0.5), "\n")
  cat("td_update :", td_update(0.5, 0.0, 0.9, 1.0, 0.1), "\n")
}
main()
