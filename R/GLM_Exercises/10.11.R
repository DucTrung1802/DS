library(GLMsData)
library(MASS)
data(cervical)
cervical$AgeNum <- rep(c(25, 35, 45, 55), 4)
par(mfrow = c(2, 2))

# 1
with(cervical, {
  plot(Deaths / Wyears ~ AgeNum, type = "n")
  lines(Deaths / Wyears ~ AgeNum,
        lty = 1,
        subset = (Country == unique(Country)[1]))
  lines(Deaths / Wyears ~ AgeNum,
        lty = 2,
        subset = (Country == unique(Country)[2]))
  lines(Deaths / Wyears ~ AgeNum,
        lty = 3,
        subset = (Country == unique(Country)[3]))
  lines(Deaths / Wyears ~ AgeNum,
        lty = 4,
        subset = (Country == unique(Country)[4]))
  legend("topleft",
         lty = 1:4,
         legend = unique(cervical$Country))
})


# 3
cc.m0 <- glm(Deaths ~ offset(log(Wyears)) + Age + Country,
             data = cervical,
             family = poisson)
plot(rstandard(cc.m0) ~ fitted(cc.m0), main = "Poisson glm")

# 4
cc.m0Q <- glm(Deaths ~ offset(log(Wyears)) + Age + Country,
              data = cervical,
              family = quasipoisson)
plot(rstandard(cc.m0Q) ~ fitted(cc.m0Q), main = "Quasi-Poisson model")

# 5
cc.m0NB <-
  glm.nb(Deaths ~ offset(log(Wyears)) + Age + Country,
         data = cervical)
cc.m0NB <- glm.convert(cc.m0NB)
plot(rstandard(cc.m0NB) ~ fitted(cc.m0NB), main = "Neg. bin. glm")
