# Backend Programming with Python
# Homework 4 - Employees

class Employee:
    def __init__(self, name, age, gender, salary, position):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.position = position


def find_average_salary(list_employees):  # Operation 1
    avg_salary = sum([float(list_employees[i].salary) for i in range(len(list_employees))]) / len(list_employees)
    print(f'The average salary in the company is: {round(avg_salary)}')


def find_oldest_youngest(list_employees):  # Operation 2
    max_age = max([list_employees[i].age for i in range(len(list_employees))])
    min_age = min([list_employees[i].age for i in range(len(list_employees))])
    oldest_employee = [list_employees[i].name for i in range(len(list_employees)) if list_employees[i].age == max_age]
    youngest_employee = [list_employees[i].name for i in range(len(list_employees)) if list_employees[i].age == min_age]
    print(f'The oldest employee(s) is/are: {oldest_employee} with age {max_age}')
    print(f'The oldest employee(s) is/are: {youngest_employee} with age {min_age}')


def employees_in_mng(list_employees):  # Operation 3
    no_employees_mng = len(
        [list_employees[i].name for i in range(len(list_employees)) if list_employees[i].position == 'MNG'])
    print(f'There are {no_employees_mng} employees in MNG.')


def find_m_f_ratio(list_employees):  # Operation 4
    no_of_male_employees = len([list_employees[i] for i in range(len(list_employees))
                                if list_employees[i].gender == 'M'])
    no_of_female_employees = len([list_employees[i] for i in range(len(list_employees))
                                  if list_employees[i].gender == 'F'])
    m_f_ratio = no_of_male_employees / no_of_female_employees
    print(f'The male to female proportion in the company is {m_f_ratio * 100}%')


def find_employee_age_groups(list_employees):  # Operation 5
    list_ages = [int(list_employees[i].age) for i in range(len(list_employees))]
    grp_18_25 = len([i for i in list_ages if 18 <= i <= 25])
    grp_26_35 = len([i for i in list_ages if 26 <= i <= 35])
    grp_36_48 = len([i for i in list_ages if 36 <= i <= 48])
    grp_49_60 = len([i for i in list_ages if 49 <= i <= 60])
    grp_61_plus = len([i for i in list_ages if 61 <= i])
    print(f'Age Groups:\n'
          f'18-25: {grp_18_25}\n'
          f'26-35: {grp_26_35}\n'
          f'36-48: {grp_36_48}\n'
          f'49-60: {grp_49_60}\n'
          f'61+: {grp_61_plus}')


def main():
    # Input
    with open('Employees.txt', 'r', encoding='utf-8-sig') as out:
        data_list = [line.rstrip('\n').split(' ') for line in out if len(line.rstrip('\n').split(' ')) > 1]
        list_employees = list()
        for i in range(len(data_list)):
            list_employees.append(Employee(data_list[i][0], data_list[i][1], data_list[i][2], data_list[i][3],
                                           data_list[i][4]))

    find_average_salary(list_employees)
    find_oldest_youngest(list_employees)
    employees_in_mng(list_employees)
    find_m_f_ratio(list_employees)
    find_employee_age_groups(list_employees)


if __name__ == '__main__':
    main()
