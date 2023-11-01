def divided_differences(x, y):
    n = len(x)
    table = [[0] * n for _ in range(n)]

    # Fill in the first column with y-values
    for i in range(n):
        table[i][0] = y[i]

    # Calculate the divided differences
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

    return table[0]  # The first row of the table contains the divided differences


def interpolate(x, y, target_x):
    n = len(x)
    result = 0

    dd_coeffs = divided_differences(x, y)
    for i in range(n):
        term = dd_coeffs[i]
        for j in range(i):
            term *= (target_x - x[j])
        result += term

    return result

target_x = 10

# Input the number of data points for SN1
SN1x = [7,9,11,13,15,17,19,21,23]
SN1y = [30,30,29,30,31,30,30,29,30]
# Perform interpolation
result = interpolate(SN1x, SN1y, target_x)
print(f"The interpolated polynomial of SN1 at T = {target_x} is {result:.4f}")


# Input the number of data points for SN2
SN2x = [4,6,8,9,11,13,14,16,20]
SN2y = [29,29,30,31,30,30,29,28,29]
# Perform interpolation
result = interpolate(SN2x, SN2y, target_x)
print(f"The interpolated polynomial of SN2 at T = {target_x} is {result:.4f}")


# Input the number of data points for SN3
SN3x = [8, 12, 15, 16]
SN3y = [30, 31, 30, 29]
# Perform interpolation
result = interpolate(SN3x, SN3y, target_x)
print(f"The interpolated polynomial of SN3 at T = {target_x} is {result:.4f}")


# Input the number of data points for SN4
SN4x = [6, 8, 12, 14]
SN4y = [29, 29, 30, 31]
# Perform interpolation
result = interpolate(SN4x, SN4y, target_x)
print(f"The interpolated polynomial of SN4 at T = {target_x} is {result:.6f}")


#               --Output--
# The interpolated polynomial of SN1 at T = 10 is 29.4787
# The interpolated polynomial of SN2 at T = 10 is 30.6451
# The interpolated polynomial of SN3 at T = 10 is 30.6250
# The interpolated polynomial of SN4 at T = 10 is 29.3333