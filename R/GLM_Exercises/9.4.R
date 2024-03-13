# Set mean and variance
mean_logistic <- 0
variance_logistic <- 1

mean_normal <- 0
variance_normal <- 1

# Generate data points for x-axis
x_values <- seq(-5, 5, length.out = 1000)

# Calculate PDF and CDF for logistic distribution
pdf_logistic <-
  dlogis(x_values,
         location = mean_logistic,
         scale = sqrt(variance_logistic))
cdf_logistic <-
  plogis(x_values,
         location = mean_logistic,
         scale = sqrt(variance_logistic))

# Calculate PDF and CDF for normal distribution
pdf_normal <-
  dnorm(x_values, mean = mean_normal, sd = sqrt(variance_normal))
cdf_normal <-
  pnorm(x_values, mean = mean_normal, sd = sqrt(variance_normal))

# Plot PDF and CDF for logistic distribution
par(mfrow = c(2, 1))

plot(
  x_values,
  pdf_logistic,
  type = 'l',
  col = 'blue',
  ylim = c(0, 1),
  lwd = 2,
  xlab = 'x',
  ylab = 'Density',
  main = 'Logistic Distribution'
)
lines(
  x_values,
  cdf_logistic,
  col = 'red',
  lty = 2,
  lwd = 2
)
legend(
  'topleft',
  legend = c('PDF', 'CDF'),
  col = c('blue', 'red'),
  lty = c(1, 2),
  lwd = 2
)

# Plot PDF and CDF for normal distribution
plot(
  x_values,
  pdf_normal,
  type = 'l',
  col = 'blue',
  ylim = c(0, 1),
  lwd = 2,
  xlab = 'x',
  ylab = 'Density',
  main = 'Normal Distribution'
)
lines(x_values,
      cdf_normal,
      col = 'red',
      lty = 2,
      lwd = 2)
legend(
  'topleft',
  legend = c('PDF', 'CDF'),
  col = c('blue', 'red'),
  lty = c(1, 2),
  lwd = 2
)

# Reset par settings
par(mfrow = c(1, 1))
