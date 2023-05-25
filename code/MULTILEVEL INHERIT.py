# -*- coding: utf-8 -*-
"""
Created on Wed May 24 13:08:58 2023

@author: 91990
"""

class office:
    def _init_(self, office_name, num_employees):
        self.office_name = office_name
        self.num_employees = num_employees

    def display_office_info(self):
        print("Office Information:")
        print("Office Name:", self.office_name)
        print("Number of Employees:", self.num_employees)


class Account:
    def _init_(self, account_name, account_id, balance):
        self.account_name = account_name
        self.account_id = account_id
        self.balance = balance

    def display_bank_info(self):
        print("Bank Information:")
        print("Account Name:", self.account_name)
        print("Account ID:", self.account_id)
        print("Balance:", self.balance)

    def update_bank_info(self, new_account_name, new_account_id):
        self.account_name = new_account_name
        self.account_id = new_account_id

    def update_balance(self, new_balance):
        self.balance = new_balance


class Employee(office, Account):
    def _init_(self, office_name, num_employees, account_name, account_id, balance, employee_name, joining_year):
        office._init_(self, office_name, num_employees)
        Account._init_(self, account_name, account_id, balance)
        self.employee_name = employee_name
        self.joining_year = joining_year

    def display_office_info(self):
        super().display_office_info()

    def display_bank_info(self):
        super().display_bank_info()

    def update_bank_info(self, new_account_name, new_account_id):
        super().update_bank_info(new_account_name, new_account_id)

    def update_balance(self, new_balance):
        super().update_balance(new_balance)


# Example usage:
employee = Employee("Main Office", 10, "John Doe", "12345", 1000.00, "Alice Smith", 2020)

employee.display_office_info()
employee.display_bank_info()

new_account_name = input("Enter new account name: ")
new_account_id = input("Enter new account ID: ")
employee.update_bank_info(new_account_name, new_account_id)

new_balance = float(input("Enter new balance: "))
employee.update_balance(new_balance)

employee.display_office_info()
employee.display_bank_info()