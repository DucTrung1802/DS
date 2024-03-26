# Create a dataframe with the provided data
data <- data.frame(
  substance = c('A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'B'),
  dose = c(0, 0.0, 20, 62.5, 100, 125.0, 200, 250.0, 500.0),
  sample = c(400, 400, 200, 200, 200, 200, 200, 200, 200),
  ab = c(3, 5, 5, 2, 14, 2, 4, 4, 7)
)
data$substance = as.factor(data$substance)


###1. Fit a binomial glm to determine if there is evidence of a difference between the two substances.
model <- glm(ab/sample ~ dose+substance, data = data, family = binomial, weights = sample)
summary(model)
#p-value=0.02 < 0.05 -> there is evidence of a difference between the two substances.

###2. Use the dose and the logarithm of dose as an explanatory variable in separate glms, and compare. 
#Which is better, and why?
model1 <- glm(ab/sample ~ dose, data = data, family = binomial, weights = sample)
summary(model1)
log(data$dose)
model2 <- glm(ab/sample ~ log(dose), data = data, family = binomial, weights = sample)
summary(model2)
#Log(dose) model produces error since dose contains 0 values. Therefore, the first model is better.

###3. Compute the 95% confidence interval for the dose regression parameter,and interpret.
confint(model1, 'dose', level = 0.95)
#This interval suggests that we can be 95% confident that the true value of the parameter lies between (-0.0001275063) and (0.0032772668).
#This is approximate 0, meaning that does does not have significant effect.

###4. Why would estimation of the ed50 be inappropriate?
#The estimation of the ED50 would be inappropriate in the context of the chromosome aberration assays mentioned in the web page 
#because the ED50, which stands for "median effective dose," is typically used to describe the point at which a substance causes 
#an effect in 50% of the population for dose-response studies related to toxicity, drug efficacy, or other biological responses. 
#In the case of chromosome aberration assays, the focus is on detecting structural changes in chromosomes rather than measuring 
#a response to varying doses, making the concept of ED50 irrelevant to the study's objectives. The assays aim to compare the 
#effects of different substances on cells, not to determine a dose that affects half of a population. Therefore, the ED50 is not 
#a suitable measure for this type of analysis.