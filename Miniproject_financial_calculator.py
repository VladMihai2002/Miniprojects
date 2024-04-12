# The Python program defines a class called financial_calculator. Let’s break down what this class does:
#
# Class Name: financial_calculator
# Attributes:
# initial_balance: Represents the initial balance for the year (input by the user).
# monthly_incomes: A list to store monthly income values (input by the user).
# monthly_expenses: A list to store monthly expense values (input by the user).
# month_names: A list of month names (“January” to “December”).
# Methods:
# input_monthly_data(month): Takes input for income and expenses for a given month and appends them to the respective lists.
# calculate_monthly_balance(month): Calculates the balance (income minus expenses) for a specific month.
# analyze_expenses(): Identifies the month with the highest expenses.
# display_final_balance(): Calculates and displays the final balance after 12 months.
# Example Usage:1
#
# The program prompts the user to input the initial balance for the year.
# It then collects monthly income and expense data for each of the 12 months.
# For each month, it calculates the balance and displays it.
# It identifies the month with the highest expenses.
# Finally, it shows the final balance after 12 months.
# Feel free to run this program and input your own financial data!

class financial_calculator:
    def __init__(self):
        self.initial_balance = float(input("Enter the initial balance for the year: "))
        self.monthly_incomes = []
        self.monthly_expenses = []
        self.month_names = ["January", "February", "March", "April", "May", "June",
                            "July", "August", "September", "October", "November", "December"]

    def input_monthly_data(self, month):
        income = float(input(f"Enter income for {month}: "))
        self.monthly_incomes.append(income)

        expense = float(input(f"Enter expenses for {month}: "))
        self.monthly_expenses.append(expense)

    def calculate_monthly_balance(self, month):
        return self.monthly_incomes[month] - self.monthly_expenses[month]

    def analyze_expenses(self):
        max_expense_month = self.month_names[self.monthly_expenses.index(max(self.monthly_expenses))]
        return max_expense_month

    def display_final_balance(self):
        final_balance = self.initial_balance + sum(self.monthly_incomes) - sum(self.monthly_expenses)
        print(f"Final balance after 12 months: ${final_balance:.2f}")

# Example usage:
if __name__ == "__main__":
    budget = financial_calculator()

    for month in range(12):
        budget.input_monthly_data(budget.month_names[month])

    for month in range(12):
        balance = budget.calculate_monthly_balance(month)
        print(f"{budget.month_names[month]} balance: ${balance:.2f}")

    max_expense_month = budget.analyze_expenses()
    print(f"The month with the highest expenses is {max_expense_month}.")

    budget.display_final_balance()