#The responses of the tobacco budworm Heliothis virescens to doses of pyrethroid trans-cypermethrin were recorded (Table 9.9; data set:budworm) [2, 23] from a small experiment. Twenty male and twenty female moths were exposed at each of six doses of the pyrethroid, and the number killed was recorded.
library('GLMsData')
data(budworm)
summary(budworm)
print(budworm)
#1. Plot survival proportions against dose, distinguishing male and female moths. Explain why using the logarithms of dose as a covariate is sensible given the values used for the pyrethroid dose.
# Calculate survival proportions
budworm$Survival <- (budworm$Number - budworm$Killed) / budworm$Number
#Plot survival proportions against dose, distinguishing male and female moths.
library(ggplot2)
ggplot(budworm, aes(x = log2(Dose), y = Survival, color = Gender)) +
  geom_point() +
  labs(title = "Survival Proportions vs. Dose",
       x = "Log2(Dose)",
       y = "Survival Proportions") +
  theme_minimal()
#Explain why using the logarithms of dose as a covariate is sensible given the values used for the pyrethroid dose.
#Because:
#- The range of dose values can vary significantly.=> Using the logarithm of dose helps spread out the data points on a plot, making it easier to visualize the relationship between dose and response.
#- Biological responses often follow a logarithmic scale. => Small changes in dose at low levels can lead to large changes in response, but the same absolute increase in dose results in smaller changes at high doses.
#- Taking the logarithm of dose can homogenize the variability across different dose levels.
#- Transforming the dose using logarithms can linearize relationships.
#2. Fit a binomial glm to the data, ensuring a diagnostic analysis. Begin by fitting a model with a systematic component of the form 1 + log2(Dose)* Gender, and show that the interaction term is not significant. Hence refit the model with systematic component 1 + log2(Dose) + Gender.
# Fit the initial model with interaction term
model_interaction <- glm(Survival ~ 1 + log2(Dose) * Gender,
                         data = budworm,
                         family = binomial(link = "logit"))
# Check significance of interaction term
summary(model_interaction) #p-value of log2(Dose),GenderM, >0.05 => the interaction term is not significant
# Refit the model without interaction
model_no_interaction <- glm(Survival ~ 1 + log2(Dose) + Gender,
                            data = budworm,
                            family = binomial(link = "logit"))
# Summary of the refitted model
summary(model_no_interaction) #p-value of log2(Dose),GenderM, >0.05 => the interaction term is not significant but better than the before model
#3. Plot the fitted lines on the plot of the data (distinguishing between males and females) and comment on the suitability of the model.

#4. Determine the odds ratio for comparing the odds of a male moth dying to the odds to a female moth dying

#5. Determine if there is any evidence of a difference in the mortality rates between the male and female moths.

#6. Determine estimates of the ed50 for both genders

#7. Determine the 90% confidence interval for the gender effect
