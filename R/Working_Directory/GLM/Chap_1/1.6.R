library("GLMsData")
data("turbines")

df = turbines
# 1.
name = names(df)

head(df)

# 2.
# All variables are quantitative

# 4.
summary(df)

# 5.
plot(Fissures/Turbines ~ Hours, data=turbines, las=1)

# 6.
# Turbines with more working hours tend to have more fissures

# 7.
# Linear regression model seem appropriate since it fit the data quite well

# 8.
?turbines
# => experimental study




