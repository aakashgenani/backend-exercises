# Backend Programming with Python
# Homework 3 - OOP

def main():

    class RestaurantStaff:
        def __init__(self, name, phone, email, address, salary):
            self.name = name
            self.phone = phone
            self.email = email
            self.address = address
            self.salary = salary

    class Chef(RestaurantStaff):
        def __init__(self, name, phone, email, address, salary, cuisine_expertise, experience):
            super().__init__(name, phone, email, address, salary)
            self.cuisine_expertise = cuisine_expertise
            self.experience = experience

        def take_dish_name(self):
            pass

        def prep_dish(self):
            pass

        def __gt__(self, other):
            if isinstance(other, Chef):
                return self.experience.__gt__(other.experience)

    class RestaurantManager(RestaurantStaff):
        def __init__(self, name, phone, email, address, salary):
            super().__init__(name, phone, email, address, salary)

        def staff_payroll(self):
            pass

        def calculate_billing(self):
            pass

        def provide_bill(self):
            pass

    class Server(RestaurantStaff):
        def __init__(self, name, phone, email, address, salary):
            super().__init__(name, phone, email, address, salary)

        def fulfil_book_table_request(self):
            pass

        def take_customer_order(self):
            pass

        def send_order_to_kitchen(self):
            pass

    class Customer:
        def __init__(self, name, phone, email):
            self.name = name
            self.phone = phone
            self.email = email

        def send_book_table_request(self):
            pass

        def give_order(self):
            pass

        def ask_bill(self):
            pass

        def __eq__(self, other):
            if isinstance(other, Customer):
                return True

        def __lt__(self, other):
            if isinstance(other, Customer):
                return False

        def __gt__(self, other):
            if isinstance(other, Customer):
                return False

    # Question part 1

    aakash = Chef('Aakash Genani', '03101191692', 'aakashgenani@gmail.com', 'Munich', 10000, 'Pizza', 100)
    nigel = Chef('Nigel', '03101191692', 'nigel@gmail.com', 'Munich', 10000, 'Pizza', 50)
    aakash_c = Customer('Aakash Genani', '03101191692', 'aakashgenani@gmail.com')
    nigel_c = Customer('Nigel', '03101191692', 'nigel@gmail.com')

    print(nigel > aakash)     # Comparing instances of Chefs to check experience relation

    print(nigel_c == aakash_c)  # Comparing whether Customers are equal or not
    print(nigel_c > aakash_c)
    print(nigel_c < aakash_c)

    # Question part 2 - Scenario

    # 1. Customer assigned:
    sara = Customer('Sara', '03101191692', 'sara@gmail.com')
    # 2. Server is assigned
    nathan = Server('Nathan', '03101191692', 'nathan@gmail.com', 'Munich', 10000)
    # 3. Chef is assigned
    aakash = Chef('Aakash Genani', '03101191692', 'aakashgenani@gmail.com', 'Munich', 10000, 'Pizza', 100)

    def scenario(customer, server, chef):
        # 1. Customer books a table
        sara.send_book_table_request()
        # 2. Servers books table request
        nathan.fulfil_book_table_request()
        # 3. Server takes the order
        nathan.take_customer_order()
        # 4. Customer gives order
        sara.give_order()
        # 5. Server send order to the kitchen
        nathan.send_order_to_kitchen()
        # 6. Chefs takes the dish name and prepares the order
        aakash.take_dish_name()
        aakash.prep_dish()
        # 7. In the end the customer asks for the bill
        sara.ask_bill()
        print('Task was fulfilled')

    scenario(sara, nathan, aakash) # instances of customer, server, and chef input into the function


if __name__ == "__main__":
    main()
