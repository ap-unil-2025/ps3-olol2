"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
                # TODO: Get input from
        user_input = input("Enter a number (or 'done' to finish): ").strip().lower()
                # TODO: Check if user typed 'done'
        if user_input =="done" :
            break
                # TODO: Try to convert to float and add to list
        try:
            num = float(user_input)
            numbers.append(num)
                # TODO: Handle invalid input gracefully
        except ValueError:
            print("Invalid input, please enter a numeric value or 'done'.")

    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}

    # TODO: Calculate count
    analysis["count"] = len(numbers)
    # TODO: Calculate sum
    analysis["sum"] = sum(numbers)
    # TODO: Calculate average
    analysis["average"] = sum(numbers)/len(numbers)
    # TODO: Find minimum
    analysis["minimum"] = min(numbers)
    # TODO: Find maximum
    analysis["maximum"] = max(numbers)
    # TODO: Count even numbers (hint: use modulo operator)
    is_even = lambda x: x.is_integer() and int(x) % 2 == 0
    analysis["even_count"] = len(list(filter(is_even, numbers))) 
    # TODO: Count odd numbers
    is_odd = lambda x: x.is_integer() and int(x) % 2 != 0
    analysis["odd_count"] = len(list(filter(is_odd, numbers))) 
    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        print("No data to display.")
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    print(f"Count : {analysis['count']}")
    # Sum: 25
    print(f"Sum : {analysis['sum']:.2f}")
    # Average: 5.00
    print(f"Average : {analysis['average']:.2f}")
    # Minimum
    print(f"Minimum : {analysis['minimum']}")
    #Maximum
    print(f"Maximum : {analysis['maximum']}")
    #Even count
    print(f"Even count : {analysis['even_count']}")
    #Odd count
    print(f"Odd count : {analysis['odd_count']}")
    pass


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()