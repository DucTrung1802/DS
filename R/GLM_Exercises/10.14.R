# Load required library
library(GLMsData)

# Load dataset
data(ants)

# Explore the dataset
str(ants)
summary(ants)

# Fit Poisson models with different combinations of predictors
model1 <- glm(Srich ~ Habitat, data = ants, family = "poisson")
model2 <- glm(Srich ~ Elevation, data = ants, family = "poisson")
model3 <- glm(Srich ~ Latitude, data = ants, family = "poisson")
model4 <- glm(Srich ~ Habitat + Elevation, data = ants, family = "poisson")
model5 <- glm(Srich ~ Habitat * Elevation, data = ants, family = "poisson")
model6 <- glm(Srich ~ Habitat + Latitude, data = ants, family = "poisson")
model7 <- glm(Srich ~ Habitat * Latitude, data = ants, family = "poisson")
model8 <- glm(Srich ~ Elevation + Latitude, data = ants, family = "poisson")
model9 <- glm(Srich ~ Elevation * Latitude, data = ants, family = "poisson")
model10 <- glm(Srich ~ Habitat * Elevation + Latitude, data = ants, family = "poisson")
model11 <- glm(Srich ~ Habitat * Latitude + Elevation , data = ants, family = "poisson")
model12 <- glm(Srich ~ Habitat * Elevation * Latitude, data = ants, family = "poisson")

# Compare models based on AIC
aic_values <- AIC(model1, model2, model3, model4, model5, model6, model7, model8, model9, model10, model11, model12)
aic_values

# Compare models based on BIC
bic_values <- BIC(model1, model2, model3, model4, model5, model6, model7, model8, model9, model10, model11, model12)
bic_values

# Select the model with the lowest AIC value
best_model_index_aic <- which.min(unlist(aic_values))
best_model_summary <- summary(get(paste0("model", best_model_index_aic)))
best_model_summary

# Select the model with the lowest BIC value
best_model_index_bic <- which.min(unlist(bic_values))
best_model_summary <- summary(get(paste0("model", best_model_index_bic)))
best_model_summary