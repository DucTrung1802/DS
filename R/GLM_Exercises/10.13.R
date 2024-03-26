# 10.13. The number of severe and non-severe cyclones in the Australian region between 1970 and 2005 were recorded 
# (Table 10.16; data set: cyclones), together with a climatic index called the Ocean Niño Index, or oni. 
# The oni is a 3-month running mean of sea surface temperature anomalies; Table 10.16 shows the oni at four times during each year.
# 1. Plot the number of severe cyclones against the oni, and then plot the number of non-severe cyclones against the oni. Comment.
# 2. Fit a Possion glm to model the number of severe cyclones, and another Poisson glm for the number of non-severe cyclones.
# 3. Interpret your final models.
library('GLMsData')
data("cyclones")
print(cyclones)
#1.
#Plot the number of severe and non-severe cyclones against the JFM
plot(cyclones$JFM, cyclones$Severe, pch = 16, col = "blue",
     xlab = "Oceanic Niño Index (ONI)", ylab = "Number of Severe Cyclones",
     main = "Number of Severe Cyclones vs. ONI (JFM)")
points(cyclones$JFM, cyclones$NonSevere, pch = 16, col = "red")
legend("topright", legend = c("Severe", "Non-severe"), col = c("blue", "red"), pch = 16)
#Plot the number of severe and non-severe cyclones against the AMJ
plot(cyclones$AMJ, cyclones$Severe, pch = 16, col = "blue",
     xlab = "Oceanic Niño Index (ONI)", ylab = "Number of Severe Cyclones",
     main = "Number of Severe Cyclones vs. ONI (AMJ)")
points(cyclones$AMJ, cyclones$NonSevere, pch = 16, col = "red")
legend("topright", legend = c("Severe", "Non-severe"), col = c("blue", "red"), pch = 16)
#Plot the number of severe and non-severe cyclones against the JAS
plot(cyclones$JAS, cyclones$Severe, pch = 16, col = "blue",
     xlab = "Oceanic Niño Index (ONI)", ylab = "Number of Severe Cyclones",
     main = "Number of Severe Cyclones vs. ONI (JAS)")
points(cyclones$JAS, cyclones$NonSevere, pch = 16, col = "red")
legend("topright", legend = c("Severe", "Non-severe"), col = c("blue", "red"), pch = 16)
#Plot the number of severe and non-severe cyclones against the OND
plot(cyclones$OND, cyclones$Severe, pch = 16, col = "blue",
     xlab = "Oceanic Niño Index (ONI)", ylab = "Number of Severe Cyclones",
     main = "Number of Severe Cyclones vs. ONI (OND)")
points(cyclones$OND, cyclones$NonSevere, pch = 16, col = "red")
legend("topright", legend = c("Severe", "Non-severe"), col = c("blue", "red"), pch = 16)
# Reset the layout to default (1 plot per screen)
par(mfrow = c(1, 1))
#2. Fit a Possion glm to model the number of severe cyclones, and another Poisson glm for the number of non-severe cyclones.
# Fit Poisson GLM for severe cyclones
model_severe <- glm(Severe ~ JFM + AMJ + JAS + OND, data = cyclones, family = poisson(link = "log"))
summary(model_severe)

# Fit Poisson GLM for non-severe cyclones
model_non_severe <- glm(NonSevere ~ JFM + AMJ + JAS + OND, data = cyclones, family = poisson(link = "log"))
summary(model_non_severe)
#3. Interpret your final models
#Two models have the interaction terms that are not significant