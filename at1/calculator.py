numbers = []
for counter in range (0, 5):
    number = int(input("Enter a number: "))
    numbers.append(number)
total = 0
for number in numbers:
    total += number
average = total / (len(numbers))
print(f"The average of the numbers {numbers} is {average}")

def check_input(input_str):
    try:
        number = float(input_str)  # Use float to allow decimal numbers.
    except ValueError:
        # The input cannot be converted to a number.
        raise ValueError(f"Invalid input '{input_str}': not a number.")
    if number < 0:
        # The number is negative.
        raise ValueError(f"Invalid input '{input_str}': number is negative.")
    return number

numbers = []
total = 0
for counter in range(0, 5):
    while True:
        try:
            user_input = input("Enter a number: ")
            number = check_input(user_input)
            numbers.append(number)
            break  # Exit the loop if input is valid.
        except Exception as error:
            print(error)

for number in numbers:
    total += number
average = total / len(numbers) if numbers else 0  # Avoid division by zero.
print(f"The average of {numbers} is {average}.")