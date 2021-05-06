# Exercise #8 - Employees Continued
# Summary
In this exercise you should create a RESTful API around the functionalities of the previous
exercise #4 - Employees. So in a nutshell, create a Flask-based API with views that
consume the code you’ve implemented already.
# Essential tasks:
Create a Flask based app that when started consumes the employees file and loads its
content into the memory to work with. This means, you should not use the file to create
folders and store it’s information in individual files, unless you tackle the extra tasks, there
will be no further operations on the file done after initialization of the app.
Extend your implementation such that each employee is identified by id, starting each line
Implement an API with the following GET endpoints, all replies should be in JSON format:
1. GET 'employee/count' - returns the total number of employees
2. GET 'employee/all' - returns the id and name of all employees
3. GET 'employee/{employeeId}' -returns all the information of the employee with the
given id
4. GET 'employee/age-group?min={ageGroupMin}&max={ageGroupMax}' - return the id
and name of all employees in parametrized age group (note: both min and max are
optional, if one is not specified then the specific limit is not bounded, a.k.a there is no
lower/upper limit)
5. GET 'department/all' - returns the codes of all departments and the total budget
6. GET 'department/budget' - returns the total budget needed and the departments that
consume the max resp. min budget
7. GET 'department/{departmentCode}/budget' - returns the total budget required by a
department.
8. GET 'department/{departmentCode}/employees' - returns a list of all employees in a
given department
# EXTRA #1
Add the following three endpoints for adding, editing and deleting customers.
1. PUT '/employee' - to add a new employee (note that you can't have two employees
with the same id!)
2. POST '/employee' - to update an existing employee
3. DELETE '/employee/{employeeId}' - to delete an employee
# EXTRA #2
Validate resource existence (employee, department etc.) where applicable and return a
proper "Not Found" status code if this validation fails.
Annex
For your convenience, here is an excerpt of the exercise #4 with the essential informations:
- Each line contains information about one employee.
- The informations (fields) are the following for all employees, fields are separated by a
blank space, always in the same order:
  - Name
  - Age
  - Gender (‘M’ or ‘F’)
  - Salary (decimal value, up to 2 digits after decimal point)
  - Position resp. Department
- All data is correct (don’t worry about validating it)

Please read the information from the file inside an in-memory structure, preferably a list.
Here are two recommended approaches for the elements in the list (pick whichever is easier
for you): List of tuples, List of objects
# Operations
Once the data is read, please write a separate function that takes the data as an input and
returns the result required by the exercise.
1. What is the average salary in the company?
2. What is the name of the oldest employee? What about the youngest?
3. How many employees are occupying the MNG position?
4. What is the Male/Female proportion in the company? (e.g.: 80%/20%)
5. How many employees are there for each of the following age groups: 18-25, 26-35,
36-48, 49-60, 61+?
# Extra:
6. How many employees are there for each department (position)?
7. Which department (position) requires the most budget (in terms of salary)?
8. What is the average between the best and worst salary for each department
(position)?
9. Who are the two employees with the closest salaries?
10. For each department, who is the employee with the salary closest to the average
salary of that department (position)?
