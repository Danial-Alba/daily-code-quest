# Digit Difference Game

## Problem Description
Implement a function that takes a two-digit number and returns the difference between its larger digit and smaller digit.

## Game Rules
- Farhad gives Salib a two-digit number
- Salib must subtract the smaller digit from the larger digit
- If digits are equal, return 0

## Function Specification
```python
def game(number: int) -> int:
    """
    Calculate the difference between larger and smaller digits of a two-digit number.
    
    Args:
        number (int): A two-digit number (10-99)
        
    Returns:
        int: Difference between larger and smaller digits
    """
