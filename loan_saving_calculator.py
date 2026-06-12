import math

def loan_calculator():
    print("\n--- Loan Calculator ---")

    principal = float(input("Enter loan amount: "))
    annual_rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter loan duration (years): "))

    monthly_rate = annual_rate / 100 / 12
    months = years * 12

    emi = principal * monthly_rate * ((1 + monthly_rate) ** months)
    emi = emi / (((1 + monthly_rate) ** months) - 1)

    total_payment = emi * months
    total_interest = total_payment - principal

    print("\nLoan Summary")
    print(f"Monthly EMI: {emi:.2f}")
    print(f"Total Payment: {total_payment:.2f}")
    print(f"Total Interest: {total_interest:.2f}")

def savings_calculator():
    print("\n--- Savings Calculator ---")

    monthly_saving = float(input("Monthly saving amount: "))
    annual_rate = float(input("Expected annual return (%): "))
    years = int(input("Number of years: "))

    monthly_rate = annual_rate / 100 / 12
    months = years * 12

    future_value = monthly_saving * (
        ((1 + monthly_rate) ** months - 1) / monthly_rate
    )

    print("\nSavings Summary")
    print(f"Future Value: {future_value:.2f}")

while True:
    print("\n========== Smart Finance Dashboard ==========")
    print("1. Loan Calculator")
    print("2. Savings Calculator")
    print("3. Exit")

    choice = input("Select option: ")

    if choice == "1":
        loan_calculator()

    elif choice == "2":
        savings_calculator()

    elif choice == "3":
        print("Thank you for using Smart Finance Dashboard")
        break

    else:
        print("Invalid choice")