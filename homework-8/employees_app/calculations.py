class Employee(object):

    def __init__(self, ident: str, name: str, age: int,
                 gender: str, salary: float, department: str):
        self._ident = ident
        self._name = name
        self._age = age
        self._gender = gender
        self._salary = salary
        self._department = department

    @property
    def id(self): return self._ident

    @property
    def name(self): return self._name

    @property
    def age(self): return self._age

    @property
    def gender(self): return self._gender

    @property
    def salary(self): return self._salary

    @property
    def department(self): return self._department

    def __str__(self):
        return f"ID {self.id}, {self.name}, age {self.age}, {self.gender}, " \
               f"from department {self._department}, earning ${self.salary}"


def employees_count(employees_list):
    return len(employees_list)


def get_employee_with_id(employees_list, employee_id):
    return list(map(lambda x: (x.id, x.name, x.age, x.gender, x.department, x.salary),
                    filter(lambda x: x.id == employee_id, employees_list)))


def departments_with_budget(employees_list):
    budget = []
    departments = list(set(map(lambda x: x.department, employees_list)))
    for i in range(len(departments)):
        budget.append((departments[i],
                       round(sum(map(lambda x: x.salary,
                                     filter(lambda x: x.department == departments[i], employees_list))), 2)))
    return dict(budget)


def total_budget(employees_list):
    return sum(map(lambda x: x.salary, employees_list))


def min_max_budget_consuming_departs(employees_list):
    maximum = max(departments_with_budget(employees_list), key=departments_with_budget(employees_list).get)
    minimum = min(departments_with_budget(employees_list), key=departments_with_budget(employees_list).get)
    return maximum, minimum


def get_depart_budget(employees_list, department_code):
    return sum(map(lambda x: x.salary, filter(lambda x: x.department == department_code, employees_list)))


def get_employees_in_depart(employees_list, department_code):
    return filter(lambda x: x.department == department_code, employees_list)
