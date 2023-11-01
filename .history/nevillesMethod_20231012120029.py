def nevilles_method(x, y, target_x):
    n = len(x)
    Q = [[0] * n for _ in range(n)]

    for i in range(n):
        Q[i][0] = y[i]

    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i][j] = ((target_x - x[i - j]) * Q[i][j - 1] - (target_x - x[i]) * Q[i - 1][j - 1]) / (x[i] - x[i - j])

    return Q[n - 1][n - 1]

target_x = 10

# Input the number of data points for SN1
SN1x = [7,9,11,13,15,17,19,21,23]
SN1y = [30,30,29,30,31,30,30,29,30]
# Perform interpolation
result = nevilles_method(SN1x, SN1y, target_x)
print(f"The interpolated polynomial of SN1 at T = {target_x} is {result:.4f}")


# Input the number of data points for SN2
SN2x = [4,6,8,9,11,13,14,16,20]
SN2y = [29,29,30,31,30,30,29,28,29]
# Perform interpolation
result = nevilles_method(SN2x, SN2y, target_x)
print(f"The interpolated polynomial of SN2 at T = {target_x} is {result:.4f}")


# Input the number of data points for SN3
SN3x = [8, 12, 15, 16]
SN3y = [30, 31, 30, 29]
# Perform interpolation
result = nevilles_method(SN3x, SN3y, target_x)
print(f"The interpolated polynomial of SN3 at T = {target_x} is {result:.4f}")


# Input the number of data points for SN4
SN4x = [6, 8, 12, 14]
SN4y = [29, 29, 30, 31]
# Perform interpolation
result = nevilles_method(SN4x, SN4y, target_x)
print(f"The interpolated polynomial of SN4 at T = {target_x} is {result:.4f}")


#               --Output--
# The interpolated polynomial of SN1 at T = 10 is 29.4787
# The interpolated polynomial of SN2 at T = 10 is 30.6451
# The interpolated polynomial of SN3 at T = 10 is 30.6250
# The interpolated polynomial of SN4 at T = 10 is 29.3333