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

# Input the number of data points
n = int(input("Enter the number of data points: "))

# Input x and y coordinates
x = []
y = []
for i in range(n):
    x_val = float(input(f"Enter x[{i}]: "))
    y_val = float(input(f"Enter y[{i}]: "))
    x.append(x_val)
    y.append(y_val)

# Input the target x for estimation
target_x = float(input("Enter the target x for estimation: "))

# Perform interpolation
estimated_value = interpolate(x, y, target_x)

print(f"The estimated value at x = {target_x} is {estimated_value:.4f}")
