def narcissistic(value):
    numbers = [int(char) for char in str(value)]
    power = len(numbers)
    sum = 0
    for number in numbers:
        sum = sum + number ** power
    if value == sum:
        return True
    return False

# numbers = [int(char) for char in str(value)]
# sum = sum([number ** len(numbers) for number in numbers])
# return value == sum


print(narcissistic(371))
print(narcissistic(122))
