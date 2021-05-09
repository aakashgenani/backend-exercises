# Homework 10 - Relational Tables
Define a relational database with tables that store information about the following three
entities:
- Authors - Name, Year of Birth, Location, Telephone, Primary Publisher
- Publishers - Name, Location, Telephone, Founding Year
- Books - Title, First Author, Second Author, Publisher, Year of Publication

Define the correct table structures and relations keeping in mind:
- Each table should have a primary key
- Relationships between tables should be implemented via foreign key
- To decide which information is mandatory and which is not it’s a good idea to check
the upcoming queries
-Insert appropriate data in your tables - notice the order of insertion will be influenced by the
relations between the tables.

Write the following queries:
1. All book titles with their first author name and publisher name
2. Author names whose primary publishers were founded after the year 2000
3. Titles of books for which the first author’s primary publisher differs from the book’s
publisher
4. Books for which the first author does not have a primary publisher
5. Books for which none of the authors have a primary publisher
6. Information (name, year of birth, location, phone) about authors that are not the First
Author of any book
7. Information about authors that are not the First or Second Author of any books
