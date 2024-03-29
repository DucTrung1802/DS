# Câu 1
my_data1 = read.csv("TuoiThoBongDen.csv")
my_data1

before = my_data1$Truoc.Cai.Tien.KT
after = my_data1$Sau.Cai.Tien.KT

# Kiểm tra dữ liệu tuân theo phân phối chuẩn
shapiro.test(before)
shapiro.test(after)

# => Vì p_value của dữ liệu trước và sau cải tiến đều thấp hơn 0.05
# => Phải dùng kiểm định phi tham số

# => Vì bóng đèn trước và sau cải tiến là độc lập nên
# Ta sử dụng Mann-Whitney U Test

# H0: Bóng đèn trước và sau cải tiến không khác nhau: mu_1 = mu_2
# H1: Bóng đèn sau cải tiến tốt hơn: mu_1 < mu_2

wilcox.test(
  before,
  after,
  exact = F,
  conf.int = T,
  paired = F,
  alternative = "less",
)

# Vì p_value = 0.0874 > 0.05
# Ta chấp nhận giả thuyết H0
# Bóng đèn trước và sau cải tiến không khác nhau với mức ý nghĩa 0.05


# Câu 2
load("births2006.smpl.rda")
my_data2 = births2006.smpl
my_data2

# a
vaginal = my_data2[my_data2$DMETH_REC == "Vaginal", ]
c_section = my_data2[my_data2$DMETH_REC == "C-section", ]

vaginal_weight = vaginal$DBWT
c_section_weight = c_section$DBWT

vaginal_weight_non_na = na.omit(vaginal_weight)
c_section_weight_non_na = na.omit(c_section_weight)

library(nortest)
ad.test(vaginal_weight_non_na)
ad.test(c_section_weight_non_na)

# Vì cả 2 bộ dữ liệu độc lập và đều không có tính chuẩn
# nên phải dùng kiểm định phi tham số cho dữ liệu độc lập.

# H0: Trọng lượng trung bình trẻ sơ sinh ở các bà mẹ sinh thường
# và các bà mẹ sinh mổ như nhau. mu1 = mu2

# H1: Trọng lượng trung bình trẻ sơ sinh ở các bà mẹ sinh thường
# và các bà mẹ sinh mổ khác nhau. mu1 != mu2

wilcox.test(
  vaginal_weight_non_na,
  c_section_weight_non_na,
  paired = F,
  conf.level = 0.99
)

# Vì p_value nhỏ hơn 0.01 nên ta bác bỏ giả thiết H0
# Trọng lượng trung bình trẻ sơ sinh ở các bà mẹ sinh thường
# và các bà mẹ sinh mổ khác nhau với mức ý nghĩa 0.01.

# b
my_data2b = table(my_data2$DOB_WK, my_data2$DMETH_REC)
my_data2b
chisq.test(my_data2b)

# Vì p_value rất nhỏ => Bác bỏ H0.

# c
my_data2c = my_data2[my_data2$DMETH_REC == "Vaginal", ]
my_data2c = my_data2c$SEX
my_data2c_non_na = na.omit(my_data2c)

my_data2c_non_na

male = my_data2c_non_na[my_data2c_non_na == "M"]
female = my_data2c_non_na[my_data2c_non_na == "F"]

k_male = length(male)
k_female = length(female)
n = length(my_data2c_non_na)

prop.test(c(k_male, k_female), c(n, n), conf.level = 0.95)

# Vì p_value rất nhỏ nên ta bác bỏ giả thiết H0

# d

library(MASS)
my_data2d = as.vector(na.omit(my_data2$DBWT))
my_data2d

# Trước tiên mình phải tìm phân phối của dữ liệu

library(MASS)
result = fitdist(my_data2d, "gamma")
summary(result)

x = rgamma(100000, shape = 22.66355, rate = 0.0069418)
var(x)
mean(x)

hist(x, freq = F)

# Câu 3
my_data3 = read.csv("Thoigiansong.csv", check.names = F)
my_data3$A
