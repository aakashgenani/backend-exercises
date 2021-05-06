# Objective:
The objective of this assignment is to practice creating classes, their
methods and how one class interacts with another. You will also have to identify the
application of OOP principles.
Problem Statement: We shall create a small program for a restaurant_staff (first
object) and how the customer (second object) interacts with the restaurant_staff.
Build following classes for restaurant related persons:
1. Chef -
- It has name, phone, email, address, salary, cuisine_expertise as data
variables.
- It has take_dish_name() and prep_dish() methods.
2. Restaurant_manager -
- It has name, phone, email, address, salary as data variables.
- It has staff_payroll(), calculate_billing() and provide_bill() methods.
3. Servers -
- It has name, phone, email, address, salary as data variables.
- It has fulfill_book_table_request(), take_customer_order() and
send_order_to_kitchen() methods.
4. Customer -
- It has name, phone, email as data variables.
- It has send_book_table_request(), give_order() and ask_bill() as methods.
NOTE: You are not required to implement the methods. Just declare the method in the
right class and write down in comments (in the code file itself) the interaction between
methods. Do not forget to identify the application of OOP principles. For simplicity, keep
all variables and methods public.
Write (at least) one base class, e.g., the classes Chef, Restaurant_manager and
Servers all come under restaurant staff and derive child classes from the base class.
Write magic functions that model the following relations:
- Chefs are ranked by its cuisine experience, this means a chef is ranked higher if
she/he has more experience.
- Customer is king, any customer shall be considered equal to another customer
Tell a story and write a method that mimics some interaction of a typical restaurant
scenario, e.g., a customer arrives, places an order, receives a bill, etc. The method
should have at least five method calls of the instantiated objects involved...
