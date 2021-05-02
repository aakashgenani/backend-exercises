# Python Revision
# I.
  You’re given an input file which contains a text.
  For each letter (regardless of casing), count how many times it appears in the text. Then
  write this result in a separate file:
  - only write the information for letters that appear
  - from frequent letters should be outputted first
  - If multiple letters share the same frequency, print them in alphabetical
  (lexicographic) order
  Example:
  Input file=“And together they walked back through the gateway to the Muggle world.”
  Output file=”t: 8, e: 8, h: 6, a: 5, g: 5, o: 4, d: 3, r: 3, w: 3, l: 3, y: 2, k: 2, u: 2, n: 1, b: 1, c: 1, m: 1”
  Can you do it without reading the entire content of the file at once?

# II.
  Given an ordered list of numbers and a specific number, we need to determine
  whether that number belongs to the list.
  Examples:
  List = [1,3,5,7,9,15,20]
  Number = 6 -> result: No doesn’t belong
  Number = 9 -> result: Yes, belongs
  Note: Always assume the list is ordered! Don’t bother to check, we don’t care what your
  program will output in case the list is not ordered.
  1. Implement this iteratively (without recursion) without using a built-in Python function
  2. [EXTRA] Implement it using recursion. Some hints for an efficient implementation:
    a. Don’t forget your list is ordered. This is essential!
    b. The element in the middle of the list carries powerful meaning!
    c. With one move, half of the list is gone!
  3. [EXTRA EXTRA] Can you also return the index of the element? (if it the element appears
  multiple times doesn’t matter which of them you pick)
