# Homework 13 - SQLAlchemy

Submit a pull request for this assignment: Create a branch before starting the
assignment, then you can create a pull request from github UI.

Use the tables defined in the previous SQL assignment (described below).
Define a relational database with tables that store information about the following three entities:
- Authors - Name, Year of Birth, Location, Telephone, Primary Publisher
- Publishers - Name, Location, Telephone, Founding Year
- Books - Title, First Author, Second Author, Publisher, Year of Publication

Create models for these classes and implement the following views in a flask app:

1. Get books (allow filtering by title, author)
2. Get Best-selling authors (authors with most books)
3. Get authors affiliated to a publication
4. Get Books affiliated to a publication
5. Get list of authors from a country
6. Get book released between a start_date and end_date
7. Add new book
8. Update the telephone number of an author
