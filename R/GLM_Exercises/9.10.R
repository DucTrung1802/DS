#The Independent newspaper tabulated the gender of all candidates running for election in the 1992 British general election
library(GLMsData)
data(belection)
print(belection)
#1. Plot the proportion of female candidates against the Party, and comment.
install.packages("dplyr")
library(dplyr)
par(mfrow = c(1, 1, 1, 1))
party_proportions <- belection %>%
  group_by(Party) %>%
  summarise(FemaleProportion = sum(Females) / (sum(Females) + sum(Males)))
barplot(party_proportions$FemaleProportion, names.arg = party_proportions$Party,
        col = "red", main = "Proportion of Female Candidates by Party",
        xlab = "Party", ylab = "Proportion of Female Candidates")
#2. Plot the proportion of female candidates against the Region, and comment.
region_proportions <- belection %>%
  group_by(Region) %>%
  summarise(FemaleProportion = sum(Females) / (sum(Females) + sum(Males)))

barplot(region_proportions$FemaleProportion, names.arg = region_proportions$Region,
        col = "salmon", main = "Proportion of Female Candidates by Region",
        xlab = "Region", ylab = "Proportion")
#3. Find a suitable binomial glm, ensuring a diagnostic analysis.
model <- glm(cbind(Females, Males) ~ Party + Region, data = belection, family = binomial())
summary(model)
#4. Is overdispersion evident?
residual_deviance <- model$deviance
degrees_of_freedom <- model$df.residual
if (residual_deviance > degrees_of_freedom) {
  print("Overdispersion is evident.")
} else {
  print("No overdispersion detected.")
}
#5. Interpret the fitted model.
print("Interpretation of coefficients:")
print(summary(model)$coefficients)
#6. Estimate and interpret the odds of a female candidate running for the Conservative and Labour parties. Then compute the odds ratio of the Conservative party fielding a female candidate to the odds of the Labour fielding a female candidate.
conservative_odds <- exp(coef(model)["PartyCons"])
labour_odds <- exp(coef(model)["PartyLabour"])
odds_ratio <- conservative_odds / labour_odds

print(paste("Odds of a female candidate running for Conservative:", round(conservative_odds, 2)))
print(paste("Odds of a female candidate running for Labour:", round(labour_odds, 2)))
print(paste("Odds ratio (Conservative vs. Labour):", round(odds_ratio, 2)))
#7. Determine if the saddlepoint approximation is likely to be suitable for these data
print("Saddlepoint approximation suitability needs further analysis.")