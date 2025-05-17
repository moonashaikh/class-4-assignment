try:
    numerator = 10
    denominator = 0
    result = numerator / denominator  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Execution completed.")
