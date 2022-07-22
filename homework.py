"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""
import time


class CashRegister:

    def __init__(self):
        self.total_price = float(0)
        self.item_list = []

    def add_item(self, item_name, item_price):
        self.total_price += float(item_price)
        self.item_list.append({'name': item_name, 'price': item_price})

    def remove_item(self, item_name):
        for item in self.item_list:
            if item_name == item['name']:
                self.item_list.remove(item)
                self.total_price -= item['price']
                print(f"\nhold on, while item is removed from list")
                time.sleep(2)
                print(f"{item_name} has been removed successfully")
                print("Updating cart...")
                time.sleep(2)
                break

    def apply_discount(self, promo_discount):
        discount = (self.total_price * promo_discount) / 100
        after_discount = self.total_price - discount
        print(f"Calculating discount...")
        time.sleep(2)
        print(f"Discount: £{discount:.2f}\n"
              f"New total: £{after_discount:.2f}")

    def get_total(self):
        print(f"Total: £{self.total_price:.2f}")

    def show_items(self):
        print(f"Items present in cart: {', '.join([item['name'] for item in self.item_list])}")

    def reset_register(self):
        print("Clearing register...")
        time.sleep(2)
        print("Register cleared, ready for next transaction")
        self.item_list.clear()
        self.total_price = 0


"""
EXAMPLE code run:
"""

print("\n")
cash_reg = CashRegister()
cash_reg.add_item("Blue Cheese", 3.75)
cash_reg.add_item("Red grapes", 2.30)
cash_reg.add_item("Red Wine", 23.15)
cash_reg.add_item("Dark chocolate", 3.79)
cash_reg.add_item("prosciutto", 4.50)
cash_reg.show_items()
cash_reg.get_total()
cash_reg.remove_item('Red Wine')
print("\n")
cash_reg.show_items()
cash_reg.get_total()
print("\n")
cash_reg.apply_discount(30)
print("_________________________________________________________\n")
cash_reg.reset_register()



"""
TASK 2
Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.
"""


class Student:
    def __init__(self):
        self.students = []
        self.subjects = []

    def add_student(self):
        self.name = input("Enter your first name and last name: ").upper()
        self.age = int(input("Enter your age: "))
        self.student_id = int(input("Enter your student ID: "))
        self.specialization = " "



class CFGStudent(Student):
    def add_specialization(self):
        self.specialization = input(
            "Indicate your specialization (Software Engineering, Data Science or Fullstack): ").capitalize()
        if self.specialization == "Software" or "Data Science" or "Fullstack?":
            return self.specialization
        else:
            print("Invalid input, choose from options specified")

    def add_subject(self):
        number_of_subjects = int(input("How many subjects are on your specialization: "))
        for subject in range(number_of_subjects):
            user_input = input("Please enter the subject and the grade you got separated by a colon,"
                               "e.g. OOP:78:  ").lower()
            split = user_input.split(":")
            self.subjects.append({"subject": split[0], "grade": split[1]})
        print(self.subjects)

    def remove_subject(self):
        remove_sub = input("What subject would you like to remove?: ").lower()
        for item in self.subjects:
            if remove_sub == item['subject']:
                self.subjects.remove(item)
                print(f"Updated list of subjects: {self.subjects}")
            elif remove_sub != item['subject']:
                print("No item removed")
                break


    def view_subjects(self):
        return f"Subjects: {', '.join([item['subject'] for item in self.subjects])}\n"

    def get_grade(self):
        grades = [int(grade["grade"]) for grade in self.subjects]
        num_of_grades = len(grades)
        total_grades = sum(grades)
        average = total_grades / num_of_grades
        return f"{self.name}'s average grade is {average}"

    def display(self):
        print("\nStudent Details:")
        print("_________________\n")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Student_ID:", self.student_id)
        print("Specialization:", self.specialization)
        print(self.view_subjects())
        print(self.get_grade())


student = CFGStudent()
student.add_student()
student.add_specialization()
student.add_subject()
student.remove_subject()
print("\n")
student.display()

