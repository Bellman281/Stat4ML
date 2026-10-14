# Chapter 6 exercise -- Monte Carlo and TD updates (Research tier)
# level: research
# HOMEWORK: ch06_text.tex Section 3.  Rscript exercise08.R

mc_update <- function(v, G, alpha) {
  # TODO: v + alpha * (G - v)
  stop("TODO: mc_update")
}
td_error <- function(r, gamma, v_next, v) {
  # TODO: r + gamma * v_next - v
  stop("TODO: td_error")
}
td_update <- function(v, r, gamma, v_next, alpha) {
  # TODO: v + alpha * td_error(r, gamma, v_next, v)
  stop("TODO: td_update")
}

main <- function() {
  cat("mc_update :", mc_update(0.5, 1.0, 0.1), "\n")
  cat("td_error  :", td_error(0.0, 0.9, 1.0, 0.5), "\n")
  cat("td_update :", td_update(0.5, 0.0, 0.9, 1.0, 0.1), "\n")
}
main()
