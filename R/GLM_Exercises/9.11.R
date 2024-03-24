library(ggplot2)
library(statmod)

data <- data.frame(
                   lymp = c("Absent", "Absent", "Absent", "Absent", "Present", "Present", "Present", "Present"),
                   gender = c("Female", "Female", "Male", "Male", "Female", "Female", "Male", "Male"),
                   osteoid = c("Absent", "Present", "Absent", "Present", "Absent", "Present", "Absent", "Present"),
                   group_size = c(3, 2, 4, 1, 5, 5, 9, 17),
                   success = c(3, 2, 4, 1, 5, 3, 5, 6)
)

data$gender = as.factor(data$gender)
data$lymp = as.factor(data$lymp)
data$osteoid = as.factor(data$osteoid)

###1. Plot the proportion of successes against gender. 
#Then plot the proportion of successes against the presence or absence of lymphocytic infiltration.
#Comment on the relationships

plot(success/group_size ~ gender, data=data)
#Female data points are clustered around a higher proportion of successes, while Male data points tend to have a lower proportion.
#This suggests that females in the study exhibit a higher success rate compared to males.

plot(success/group_size ~ lymp, data=data)
#The absence of lymphocytic infiltration is associated with a higher proportion of successes1.
#Conversely, the presence of lymphocytic infiltration tends to result in a lower success rate.

###2. Fit the binomial glm using the gender and presence or absence of lymphocytic infiltration as explanatory variables. 
#Show that the Wald test indicate that the effect of lymphocytic infiltration is not significant.
model <- glm(success/group_size ~ lymp+gender, data = data, family = binomial, weights = group_size)
summary(model)
printCoefmat(coef(summary(model)))
#We have p-value of lymphocytic infiltration coefficient equals 0.99 -> The effect of lymphocytic infiltration is not significant

###3.Show that the likelihood ratio test indicates that the effect of lymphocytic infiltration is significant.
model2 <- glm(success/group_size ~ gender, data = data, family = binomial, weights = group_size)
anova(model2, model, test="Chisq")
#We have p-value=0.002305 < 0.05 -> The effect of lymphocytic infiltration is considered statistically significant.

###4. Show that the score test also indicates that the effect of lymphocytic infiltration is significant.
z.score <- glm.scoretest(model2, as.numeric(data$lymp))
p.score <- 2*(1-pnorm(abs(z.score)))
round( c(score.stat=z.score, P=p.score), 4)
#p-value=0.0099 < 0.05 -> Evidence suggests that the effect of lymphocytic infiltration is significant.

###5. Explain the results from the three tests.
#Wald test results show nothing greatly significant; the others do because of the Hauck–Donner effect, since y/m is always 1 when li is Absent.