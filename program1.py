result = []

# Iterate through the range from 2000 to 3200 (both included)
for number in range(2000, 3201):
    # Check if the number is divisible by 7 and not a multiple of 5
    if number % 7 == 0 and number % 5 != 0:
        result.append(str(number))

# Print the result as a comma-separated sequence on a single line
print(','.join(result))

