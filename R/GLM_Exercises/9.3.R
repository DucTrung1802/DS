library(MASS)
library(GLMsData)
data(deposit)
deposit

deposit$logDep <- log(deposit$Deposit)

ins.m3 <- glm(
  Killed / Number ~ poly(logDep, 2, raw = T) + Insecticide - 1,
  family = binomial,
  weights = Number,
  data = deposit
)

coef(ins.m3)

solve_quadratic <- function(a, b, c) {
  # Calculate the discriminant
  discriminant <- b ^ 2 - 4 * a * c
  
  if (discriminant > 0) {
    # Two real roots
    root1 <- (-b + sqrt(discriminant)) / (2 * a)
    root2 <- (-b - sqrt(discriminant)) / (2 * a)
    return(list(root1 = root1, root2 = root2))
  } else if (discriminant == 0) {
    # One real root (repeated)
    root <- -b / (2 * a)
    return(list(root1 = root, root2 = root))
  } else {
    # Complex roots
    real_part <- -b / (2 * a)
    imaginary_part <- sqrt(-discriminant) / (2 * a)
    root1 <- paste(real_part, "+", imaginary_part, "i")
    root2 <- paste(real_part, "-", imaginary_part, "i")
    return(list(root1 = root1, root2 = root2))
  }
}

ed50.A = solve_quadratic(coef(ins.m3)[2], coef(ins.m3)[1], coef(ins.m3)[3])[1]
ed50.B = solve_quadratic(coef(ins.m3)[2], coef(ins.m3)[1], coef(ins.m3)[4])[1]
ed50.C = solve_quadratic(coef(ins.m3)[2], coef(ins.m3)[1], coef(ins.m3)[5])[1]

ed50.log = cbind(ed50.A, ed50.B, ed50.C)
ed50.final = as.data.frame(lapply(ed50.log, FUN = exp))
rownames(ed50.final) = "ED50"
colnames(ed50.final) = c("Insect. A", "Insect. B", "Insect. C")
ed50.final

# Visualize data
newD <- seq(min(deposit$logDep), max(deposit$logDep), length = 30)
newProp4.logA <- predict(ins.m3,
                         type = "response",
                         newdata = data.frame(logDep = newD, Insecticide =
                                                "A"))
newProp4.logB <- predict(ins.m3,
                         type = "response",
                         newdata = data.frame(logDep = newD, Insecticide =
                                                "B"))
newProp4.logC <- predict(ins.m3,
                         type = "response",
                         newdata = data.frame(logDep = newD, Insecticide =
                                                "C"))

plot(
  1,
  type = "n",
  ylim = c(0, 1),
  xlim = c(1.5, 8),
  xlab = "Dose",
  ylab = "Kill Proportion",
  las = 1,
  xaxt = 'n',
  yaxt = 'n'
)
axis(1, at = seq(1.5, 8, 0.5))
axis(2, at = seq(0, 1, 0.1), las = 1)
lines(
  newProp4.logA ~ exp(newD),
  lty = 1,
  col = "red",
  lwd = 5,
  type = "b"
)
lines(
  newProp4.logB ~ exp(newD),
  lty = 1,
  col = "blue",
  lwd = 5,
  type = "b"
)
lines(
  newProp4.logC ~ exp(newD),
  lty = 1,
  col = "black",
  lwd = 5,
  type = "b"
)

legend(
  "topleft",
  col = c("red", "blue", "black"),
  legend = c("Insect.A", "Insect.B", "Insect.C"),
  lty = 1,
  lwd = 6,
  cex = 1,
)
