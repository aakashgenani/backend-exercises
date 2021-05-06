# Input
Please download the attached file “Employees.txt” and include it into your project. It contains
the input data for your exercise.
- Each line contains information about one employee.
- The informations (fields) are the following for all employees:
- Fields are separated by a blank space, always in the same order (as mentioned above)
  - Name
  - Age
  - Gender (‘M’ or ‘F’)
  - Salary (decimal value, up to 2 digits after decimal point)
  - Position
  - All data is correct (don’t worry about validating it)
Please read the information from the file inside an in-memory structure, preferably a list.
Here are two recommended approaches for the elements in the list (pick whichever is easier
for you):
- List of tuples
- List of objects

# Operations
Once the data is read, please write a separate function that takes the data as an input and
returns the result required by the exercise.
1. What is the average salary in the company?
2. What is the name of the oldest employee? What about the youngest?
3. How many employees are occupying the MNG position?
4. What is the Male/Female proportion in the company? (e.g.: 80%/20%)
5. How many employees are there for each of the following age groups: 18-25, 26-35, 36-48,
49-60, 61+?
# [Extra]
6. How many employees are there for each department (position)?
7. Which department (position) requires the most budget (in terms of salary)?
8. What is the average between the best and worst salary for each department (position)?
9. Who are the two employees with the closest salaries?
10. For each department, who is the employee with the salary closest to the average salary
of that department (position)?

Note: it is obvious that your program should continue functioning if the content of the file
changes. No hardcoded results please.
Note 2: New positions may also appear.
