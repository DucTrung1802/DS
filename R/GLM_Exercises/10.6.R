# 1
# log_u = beta_0 + beta_1 * C + beta_2 * M + beta_3 * M ^ 2
# log_u = -2.928 + 0.238 * C + 0.017 * M + (-0.028) * M ^ 2

# 2
res_dev = c(723.74, 662.25, 649.01, 637.22)
dev = abs(diff(res_dev))
dev
p_value.lrt = pchisq(dev, df = 1, lower.tail = F)
p_value.lrt

# => Kết luận: cả 3 biến giải thích đều có ý nghĩa cho mô hình.
# Trong đó, biến giải thích C có ảnh hưởng nhất.

# 3
beta = c(0.238, 0.017, -0.028)
se = c(0.028, 0.035, 0.009)
z = beta/se
z
p_value.wald = 2 * (1 - pnorm(abs(z)))

print("likelihood ratio test: ", paste(p_value.lrt, collapse = " "))
p_value.wald

