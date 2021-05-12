# Homework 11 - More SQL Queries

Use the tables defined in the previous assignment (described below).
Define a relational database with tables that store information about the following three entities:
- Authors - Name, Year of Birth, Location, Telephone, Primary Publisher
- Publishers - Name, Location, Telephone, Founding Year
- Books - Title, First Author, Second Author, Publisher, Year of Publication

Write the following queries:
1. Count of books per each publisher
2. Top 3 authors with most books
3. Books which are not published by the Primary Publisher of the First Author
4. The country with the most books "authored".
5. The publisher founded after the year 2000 with the most books publiished.
6. Number of authors below the age of 30 from each publisher started before 1985.
7. Which authors have the most number of books together?
8. Number of collaborations between each pair of countries (a collaboration between
countries is when authors from these countries write a bookotogether.) eg. the result
should look like:
a. Germany, France, 4
b. Germany, Austria, 30
c. Canada, India, 6
d. Canada, France, 15 ...
