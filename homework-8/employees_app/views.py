from employees_app.app import app
from employees_app import calculations, errors
from employees_app.calculations import Employee
from flask import jsonify, make_response

''' Reading the file'''
filepath = 'EmployeesWithID.txt'
with open(filepath, 'r', encoding='utf-8-sig') as file_emp:
    employees_list = []
    for line in file_emp:
        values = line.rstrip().split(' ')
        employee = Employee(
            str(values[0]), values[1], int(values[2]), values[3],
            float(values[4]), values[5])
        employees_list.append(employee)


@app.route('/')
def home():
    return "Welcome to the employees app main page!"


@app.route('/employee/count', methods=['GET'])
def get_count():
    count = calculations.employees_count(employees_list)
    return make_response(jsonify(message=f"The count of the employees is {count})"), 200)


@app.route('/employee/all', methods=['GET'])
def get_all_employees():
    all_employees = [(employee.id, employee.name) for employee in employees_list]
    return make_response(jsonify(employees=f"{all_employees}"), 200)


@app.route('/employee/<string:employee_id>', methods=['GET'])
def get_employee_details(employee_id):
    employee_details = calculations.get_employee_with_id(employees_list, employee_id)
    return make_response(jsonify(employee_details=f"{employee_details}"), 200)


@app.route('/employee/age-group/<int:age_group_min>-<int:age_group_max>', methods=['GET'])
def age_group(age_group_min: int, age_group_max: int):
    employees_filtered = list(filter(lambda x: age_group_max >= x.age >= age_group_min, employees_list))
    data = [(x.id, x.name) for x in employees_filtered]
    return make_response(jsonify(employees=f"{data}"), 200)


@app.route('/department/all', methods=['GET'])
def get_departments_budgets():
    departs_budget = calculations.departments_with_budget(employees_list)
    total_budget = calculations.total_budget(employees_list)
    return make_response(jsonify(departments=f"{departs_budget}", total_budget=f"{round(total_budget, 2)}"), 200)


@app.route('/department/budget', methods=['GET'])
def get_departments_max_min_budget():
    total_budget = calculations.total_budget(employees_list)
    maximum, minimum = calculations.min_max_budget_consuming_departs(employees_list)
    return make_response(jsonify(max=maximum, min=minimum, total=round(total_budget, 2)), 200)


@app.route('/department/<string:department_code>/budget', methods=['GET'])
def get_budget(department_code):
    budget = calculations.get_depart_budget(employees_list, department_code)
    return make_response(jsonify(budget=round(budget, 2)), 200)


@app.route('/department/<string:department_code>/employees', methods=['GET'])
def get_depart_employees(department_code):
    employees_in_depart = list(map(lambda x: x.name,
                                   calculations.get_employees_in_depart(employees_list, department_code)))
    return make_response(jsonify(employees=employees_in_depart), 200)
