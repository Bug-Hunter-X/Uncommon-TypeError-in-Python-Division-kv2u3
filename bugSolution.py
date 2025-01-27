def function_with_improved_error_handling(x, y):
    try:
        if not isinstance(y, (int, float)):
            raise TypeError("Divisor must be a number")
        if y == 0:
            raise ZeroDivisionError("Division by zero")
        result = x / y
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return f"Type Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage:
result1 = function_with_improved_error_handling(5, 0)
print(f"Result 1: {result1}")  # Output: Division by zero
result2 = function_with_improved_error_handling(5, "a")
print(f"Result 2: {result2}")  # Output: Type Error: Divisor must be a number
result3 = function_with_improved_error_handling(10, 2)
print(f"Result 3: {result3}")  # Output: 5.0