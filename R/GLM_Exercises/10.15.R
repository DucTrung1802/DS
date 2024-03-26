library(GLMsData)
data(polyps)
print(polyps)
#1. Plot the data and comment
par(mfrow = c(1, 1))
plot(polyps$Age, polyps$Number, xlab = "Age", ylab = "Number of Polyps",
     main = "Scatter Plot: Age vs. Number of Polyps")
#The scatter plot shows a positive relationship between age and the number of polyps.
#2. Find a suitable Poisson glm for modelling the data, and show that overdispersion exists.
poisson_model <- glm(Number ~ Age, data = polyps, family = poisson)
summary(poisson_model)
#The Poisson model may not be appropriate due to overdispersion (residual deviance > degrees of freedom).
#3. Fit a quasi-Poisson model to the data.
quasi_poisson_model <- glm(Number ~ Age, data = polyps, family = quasipoisson)
summary(quasi_poisson_model)
#4. Fit a negative binomial glm to the data.
library(MASS)
neg_binom_model <- glm.nb(Number ~ Age, data = polyps)
summary(neg_binom_model)
#5. Decide on a final model.
#poisson_model