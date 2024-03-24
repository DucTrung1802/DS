library("AER")
# Define the coefficients for males and females
beta_males <- c(0.45, 0.04, 0.25, 0.23)
beta_females <- c(-0.22, 0.26, 0.82, -0.22)

# Define values for Role Stress (RS) and Adolescent Aggression (AA)
RS <- 0.5
AA <- 0.3

# Compute predicted probabilities for males and females
p_males <- 1 / (1 + exp(-(beta_males[1] + beta_males[2]*RS + beta_males[3]*AA + beta_males[4]*RS*AA)))
p_females <- 1 / (1 + exp(-(beta_females[1] + beta_females[2]*RS + beta_females[3]*AA + beta_females[4]*RS*AA)))

# Interpretation
print(paste("Predicted probability of aggression in males:", p_males))
print(paste("Predicted probability of aggression in females:", p_females))

# 2. Compute and interpret the odds ratios for Role Stress
exp(beta_males[2])
exp(beta_females[2])

# 3. Compute and interpret the odds ratios for Adolescent Aggression
exp(beta_males[3])
exp(beta_females[3])

# 4. Compute and interpret the 95% confidence intervals for the interaction term
model_males <- glm(vs ~ mpg * wt, family = binomial, data = mtcars)
model_females <- glm(vs ~ mpg * wt, family = binomial, data = mtcars)

confint(model_males, "mpg:wt")
confint(model_females, "mpg:wt")

# 5. Compute and interpret the odds ratios for Adolescent Aggression
exp(beta_males[3])
exp(beta_females[3])

# 6. Check for overdispersion
# Convert logistic GLM to Poisson GLM for dispersion test
model_males_poisson <- glm(vs ~ mpg * wt, family = poisson, data = mtcars)
model_females_poisson <- glm(vs ~ mpg * wt, family = poisson, data = mtcars)

# Check for overdispersion using dispersiontest
dispersiontest(model_males_poisson)
dispersiontest(model_females_poisson)


# 7. Discuss the regression parameter for the three-way interaction RS.AA.G
# This will involve fitting a logistic GLM with the additional interaction term and interpreting the results
