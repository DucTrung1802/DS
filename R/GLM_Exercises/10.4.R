# 1
# Số chính trị gia chuyển đảng trong khoảng thời gian
# từ năm 1802 - 1876 là một con số đếm không có chặn trên
# nên mô hình GLM Poisson sẽ là mô hình phù hợp.

# 2
# Hệ số của biến giải thích cho biết năm đó có phải là
# năm bầu cử hay không (được mã hóa là 0 cho các năm bầu
# cử và 1 cho các năm không bầu cử) là 1,051 cho thấy
# rằng, tính trung bình, giá trị log của muy tăng 1.051,
# nghĩa là
# (khả năng có chính trị gia chuyển đảng cao hơn 
# exp(1.051) = 2.86 lần) nếu năm đó là năm không bầu cửa,
# giữ nguyên các tham số khác.

# 3
# Để kiểm tra ý nghĩa thống kê của hệ số cho biến giải
# "năm bầu cử". Đặt hệ số là beta_k.
# Giả thuyết H0: hệ số cho biến "năm bầu cử" không có ý
# nghĩa => beta_k = 0
# Giả thuyết H1: hệ số cho biến "năm bầu cử" có ý nghĩa
# => beta_k != 0

# install.packages("BSDA")
library(BSDA)

beta_k = 1.051
std_err = 0.320

null_hypothesis = 0

z_score = (beta_k - null_hypothesis) / std_err
p_value = 2 * pnorm(-abs(z_score))

print(paste("z_score: ", z_score))
print(paste("p_value: ", p_value))

# => Hệ số beta_k có ý nghĩa thống kê

# 4

conf_int_prob = 0.9

z_90 = qnorm((1 + conf_int_prob) / 2)
conf_int = c(beta_k - z_90 * std_err, beta_k + z_90 * std_err)

print(paste("confident_interval: ", paste(conf_int, collapse = " ")))
