# Strings
# Mandatory

1. Write a function that validates a password (regular string) based on the criterias below:
  - Must have a minimum of 8 characters. (e.g.: “Al4e2!” fails the criteria)
  - Must contain at least one upper-case letter (e.g.: “ab3cd@1efg” fails the criteria)
  - Must contain at least two digits (e.g: “Uv3!xxzy” fails the criteria)
  - Can’t contain two or more consecutive digits (e.g.: “UX525!pun” fails the criteria)

Write a program that takes as an input a password string and passes it to the function
above. Based on the outcome, notify the user whether the password is strong enough or not.

2. Manipulating words
  a. Write a function that receives a single string of words and returns the separated words
  as a list of strings.
  Example: Input=”I can go, you can’t go”. Output=[“I”, “can”, “go”, “you”, “can’t”, “go”]
  b. Write a function that takes a list of strings, and returns all the distinct strings and the
  number of times they appear in the array. Ignore capitalization. (frequency of
  appearance)
  Example: Input=”the cat the dog and the mouse”. Output=[(“the”, 3), (“cat”, 1), (“dog”, 1),
  (“and”, 1), (“mouse”, 1)]
  c. Write a function that receives the input from point b, and returns the words with the
  highest order of appearance (preferably in alphabetical (lexicographic) order).

Write a program that receives a string containing words as an input, and returns the most
frequent word(s) in that string, separated by a blank space.
E.g.: Input=”You are the best of the best”. Output=”best the”

# Extra

3. For point 1
  a. Change the main program to instead ask the user to keep inputting passwords until they
  input a correct one.
  b. Instead of only reporting whether the password is correct or not, also report to the user
  the first failed criteria.
