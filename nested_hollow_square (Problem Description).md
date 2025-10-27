markdown

# Nested Hollow Square Pattern

## Problem Description
Write a program that takes two positive integers `a` and `b` as input and draws a hollow square pattern with specific validation rules.

## Pattern Definition
- Outer square with side length `a`
- Inner hollow square with side length `b` removed from inside
- The pattern consists of asterisks (`*`) with spaces between them

## Validation Rules
1. **Wrong order!**: If inner square side (`b`) ≥ outer square side (`a`)
2. **Wrong difference!**: If the difference (`a - b`) is not even
3. Otherwise: Draw the nested hollow square pattern

## Input Specifications
- First line: integer `a` (1 ≤ a ≤ 20)
- Second line: integer `b` (1 ≤ b ≤ 20)

## Output Specifications
- Error message or the nested square pattern
- Asterisks are separated by spaces in the output
