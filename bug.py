def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Unsupported operand type(s) for /'"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage that triggers the uncommon TypeError
result = function_with_uncommon_error(5, "a")
print(result)