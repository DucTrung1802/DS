library("GLMsData")
data("paper")
df = paper
plot(
  x = df$Hardwood,
  y = df$Strength,
  xlim = c(0, 20),
  ylim = c(0, 60)
)

# Explain:
# - Choose Cubic since
# + It is more accurate than Quadratic
# + It is simpler than Quartic but quite similar