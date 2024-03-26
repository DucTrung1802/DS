library(MASS)
library(statmod)
library(GLMsData)
# 10.16. An experiment [21] compared the density of understorey birds at a
# series of sites in two areas either side of a stockproof fence (Table 10.19;
# data set: grazing). One side had limited grazing (mainly from native herbivores),
# and the other was heavily grazed by feral herbivores, mostly horses.
# Bird counts were recorded at the sites either side of the fence (the ‘before’
# measurements). Then the herbivores were removed, and bird counts recorded
# again (the ‘after’ measurements). The measurements are the total number of
# understorey-foraging birds observed in three 20-min surveys of 2 ha quadrats.

# 1. Plot the data, and explain the important features.

data(grazing)
par(mfrow = c(1, 1))
plot(Birds~When,data=grazing)
plot(Birds~Grazed,data=grazing)
#Biểu đồ thể hiện số lượng chim giảm khi có động vật ăn cỏ xuất hiện, trong đó,
#động vật hoang (Feral) làm giảm số lượng chim hơn Reference.


# 2. Fit a Poisson glm with systematic component Birds ~ When * Grazed,
# ensuring a diagnostic analysis.
poisson_model <- glm(Birds ~ When * Grazed, data = grazing, family = poisson)
summary(poisson_model)
# Mô hình này cho thấy cả hai việc loại bỏ loài cỏ ăn cỏ (When) và mức độ chăn 
# nuôi (Grazed) đều có ảnh hưởng đáng kể đến số lượng chim trong tầng dưới rừng, 
# với hiệu ứng tương tác cho thấy tác động của việc loại bỏ loài cỏ ăn cỏ biến 
# đổi tùy thuộc vào loại động vật.


# 3. Show that overdispersion exists. Demonstrate by computing the mean
# and variance of each combination of the explanatory variables.
pchisq(deviance(poisson_model), df.residual(poisson_model), lower.tail=FALSE)
#p-value=1.39e-59 < 0.05 -> Không đủ cơ sở chứng minh mô hình phù hợp -> Mô hình
#bị overdispersion.

# 4. Fit a quasi-Poisson model.
quasi_model <- glm(Birds ~ When * Grazed, data = grazing, family='quasipoisson')
summary(quasi_model)
quasi_poisson_aic_bic(quasi_model)
# 5. Fit a negative binomial glm.
nb_model <- glm.nb(Birds ~ When * Grazed, data = grazing)
summary(nb_model)
nb_model_2 <- glm.nb(Birds ~ When + Grazed, data = grazing)
summary(nb_model_2)


# 6. Compare all three fitted models to determine a suitable model.
par(mfrow = c(3, 3))
scatter.smooth( rstandard(poisson_model) ~ fitted(poisson_model), main="Poisson glm" )
scatter.smooth( rstandard(quasi_model) ~ fitted(quasi_model), main="QuasiPoisson glm" )
scatter.smooth( rstandard(nb_model) ~ fitted(nb_model), main="Negative Binomial glm" )
plot( cooks.distance(poisson_model), type="h", las=1, main="Cook's D Poisson")
plot( cooks.distance(quasi_model), type="h", las=1, main="Cook's D QuasiPoisson")
plot( cooks.distance(nb_model), type="h", las=1, main="Cook's D Negative Binomial")
qqnorm( qr<-qresid(poisson_model), ylim=c(-6,6),las=1 ); abline(0, 1)
qqnorm( qr<-qresid(quasi_model), ylim=c(-6,6), las=1 ); abline(0, 1)
qqnorm( qr<-qresid(nb_model), ylim=c(-6,6), las=1 ); abline(0, 1)

AIC(quasi_model) #Không tính được AIC của quasimodel. In quasi-models there is 
# no valid definition of a likelihood, hence no AIC, BIC etc. values.

#Dựa vào mô hình ta thấy Negative Binomial có ít outlier nhất và QQplot hợp lý nhất

# 7. Interpret the final model.
nb_model <- glm.nb(Birds ~ When + Grazed, data = grazing)
summary(nb_model)
