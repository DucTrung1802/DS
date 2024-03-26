# Libraries
library(ggplot2)
library(hrbrthemes)

# create data
xValue <- 1:10
yValue <- cumsum(rnorm(10))
data <- data.frame(xValue,yValue)

# Plot
ggplot(data, aes(x=xValue, y=yValue)) +
  geom_line( color="red", size=2, alpha=1, linetype=1) +
  theme_ipsum() +
  ggtitle("Evolution of something")