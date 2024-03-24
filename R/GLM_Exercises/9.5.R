library(aod)
# Coefficients and standard errors from Table 9.6
coefficients <- c(-6.949, 0.805, 0.161, 0.332, 0.116)
standard_errors <- c(0.3777, 0.0444, 0.0113, 0.0393, 0.0204)
variable_names <- c('Intercept','Age','Sex','Body mass','Apnoea')


# Fitted model
# log(presence of hypertension) = -6.949 + 0.805*age ....
fitted_model <- function(age, sex, bmi, ahi) {
  if (age <= 10){
    g_age <- 0
  } else {
    g_age <- 1
  }
  
  if (sex == 'males'){
    sx = 1
  } else {
    sx = 0
  }
  
  if (bmi < 5) {
    bm = 0
  } else {
    bm = 1
  }
  
  if (ahi < 10) {
    ah = 0
  } else {
    ah = 1
  }
  
  log_odds <- coefficients[1] + coefficients[2]*g_age + coefficients[3]*sx + coefficients[4]*bm + coefficients[5]*ah
  odds_ratio <- exp(log_odds)
  probability <- odds_ratio / (1 + odds_ratio)
  return(probability)
}

#Wald-test
# Loop through each coefficient

for (i in 1:5){
  print(variable_names[i])
  print(wald.test(Sigma = diag(standard_errors^2), b = coefficients, Terms = i))  
}

z <- coefficients/standard_errors
ci <- cbind( coefficients-1.96*standard_errors, coefficients+1.96*standard_errors)
pvals <- (1-pnorm(abs(z)))*2;

# 95% confidence intervals for each coefficient
conf_intervals <- matrix(0, nrow = 5, ncol = 2)
for (i in 1:5) {
  conf_intervals[i,] <- coefficients[i] + c(-1.96, 1.96) * standard_errors[i]
}

# Odds ratios for each independent variable
odds_ratios <- exp(coefficients)

# Predict the mean probability of observing hypertension
predicted_probability <- fitted_model(age = 30, sex = 1, bmi = 6, ahi = 5)

# Output the results
#cat("Wald test statistics:\n")
#print(wald_test)

cat("\n95% Confidence Intervals for coefficients:\n")
print(conf_intervals)

cat("\nOdds Ratios for each independent variable:\n")
print(odds_ratios)

cat("\nPredicted mean probability of observing hypertension for a 30-year-old male with BMI 6 and AHI 5:\n")
print(predicted_probability)
