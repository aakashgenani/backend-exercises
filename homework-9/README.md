# Backend Development with Python
# Homework 9

The homework assumes that you have setup the Bookshop database with the Books table
with the following columns:
  - Title: TEXT (NOT-NULLABLE)
  - Author: TEXT (NULLABLE)
  - Publisher: TEXT (NULLABLE)
  - Description: TEXT (NOT-NULLABLE)
  - Edition: INTEGER (NULLABLE)
  - Year: INTEGER (NOT-NULLABLE)
  - Quantity: INTEGER (NOT-NULLABLE)
  - Price: REAL (NULLABLE)

Write a separate query to retrieve the following informations:
  1. Title and Description of all books written by “J.K. Rowling”
  2. Title, Publisher and Edition of all books printed last decade (in the 2010s)
  3. All information about books that are not in stock
  4. All books in stock without a price
  5. All books containing the word “Cooking” or “Food”, in stock that were written by either
  “Gordon Ramsay” or “Jamie Oliver”
  6. All authors whose name starts with a vowel
  7. All book titles that have the letter “a” at least 3 times in.
  8. Book titles composed of exactly 4 characters.
  9. Books with the title same as the name of the author
  10. Books in stock, written by an author whose name does not end with the letter a, with a
  description that is either empty or has at least 5 characters
  
Note: It is recommended you populate the table with sufficient meaningful data to ensure you
can verify the correctness of your queries.
