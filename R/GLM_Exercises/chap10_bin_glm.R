#install.packages('GLMsData')
library(GLMsData)
data(kstones); str(kstones)
kstones
y <- ifelse(kstones$Outcome=="Success", 1, 0)

#Binomial
ks.bin <- glm(y~Size*Method, family=binomial, weights=Counts, data=kstones)
anova(ks.bin, test="Chisq")
coef(ks.bin)
#Poisson
gm.int <- glm(y~Size*Method, family=poisson, weights=Counts, data=kstones)
anova(gm.int, test="Chisq")

#Goodness-of-fit
ks.noMO <- glm( Counts ~ Size * (Method + Outcome),
                family=poisson, data=kstones ) #Contigency table
ks.noMO
pchisq(deviance(ks.bin), df.residual(ks.bin), lower.tail=FALSE)




#Pock mark data
data(pock)
m1 <- glm( Count ~ log2(Dilution), data=pock, family=poisson )
pchisq(deviance(m1), df.residual(m1), lower.tail=FALSE)

#Quasi-poisson
m.qp <- glm( Count ~ log2(Dilution), data=pock, family="quasipoisson")
summary(m.qp)
