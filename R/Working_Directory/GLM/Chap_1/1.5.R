# Linear regression model: E[y] = u = f(b0 + b1x1 + ... + bpxp)
# Generalized linear model: E[y] = g(u) = b0 + b1x1 + ... + bpxp

# 1. u = b0 + b1x1 + b2log(x2)
# => Linear in the parameters; suitable for linear regression and glms.

# 2. u = b0 + exp(b1 + b2x)
# => Not linear in parameters

# 3. u = exp(b0 + b1x) for u > 0
# => Linear in the parameters; suitable for glms

# 4. u = 1/(b0 + b1x1 + b2x1x2) for u > 0
# => Linear in the parameters; suitable for glms