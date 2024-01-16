library("GLMsData")
data("blocks")

?blocks

blocks$Trial <- factor(blocks$Trial)
blocks$cutAge <- cut(blocks$Age, breaks=c(0, median(blocks$Age), Inf))
blocks$cutAge

# 1.
summary(blocks)

# 2.
par(mfrow=c(2,4))
plot(Time ~ Shape, data=blocks, las=1)
plot(Time ~ Trial
     , data=df, las=1)
plot( Time~Age, data=blocks, las=1)
with(blocks, interaction.plot(Shape, cutAge, Time))

# 3. For both responses: shape seems important; trial number doesn’t; age possibly

# 4.
plot( Number~Shape, data=blocks, las=1)
plot( Number~Trial, data=blocks, las=1)
plot( Number~Age, data=blocks, las=1)
with(blocks, interaction.plot(Shape, cutAge, Number))

# 5.
# Perhaps interactions