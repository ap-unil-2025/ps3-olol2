"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):

    F = (float(celsius) * 9/5) + 32
    return float(F)


def fahrenheit_to_celsius(fahrenheit):

    C = (float(fahrenheit) - 32) * 5/9
    return float(C)

def temperature_converter():

    try:
        temp = (float(input("Enter the temperature value: ")))
        unit = input("Is this in Celsius or Fahrenheit? (C/F) : ").strip().upper()

        if unit == 'C':
            converted = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {converted}°F")
        
        elif unit == "F":
            converted = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {converted}°C")
        
        else:
            print( "Invalid unit! Please enter Celsius or Fahrenheit")
    except ValueError:
        print("Invalid input! Please enter a numeric temperature.")
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """


    # TODO: Implement the interactive converter
    # Remember to:
    # - Get temperature value from user
    # - Get unit (C or F) from user
    # - Validate input
    # - Perform conversion
    # - Display result rounded to 2 decimal places



# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()