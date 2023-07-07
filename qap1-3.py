# Program description:
#     This program calculates employee payroll amounts for a company called Widgets Inc.
# Written by: Evan Harte
# Date written: May 9, 2023

# Constant variables:
HOURLY_PAY_RATE = 19.50
COMMISSION_RATE = .35
INCOME_TAX_RATE = .21
CPP_RATE = .0495
EI_RATE = .016
UNION_DUES = 18.00

# Get user inputs:
EmployeeName = input("Enter employee name: ")
HoursWorked = float(input("Enter hours worked: "))
NumWidgetsMon = int(input("Enter number of widgets produced on Monday: "))
NumWidgetsTues = int(input("Enter number of widgets produced on Tuesday: "))
NumWidgetsWed = int(input("Enter number of widgets produced on Wednesday: "))
NumWidgetsThurs = int(input("Enter number of widgets produced on Thursday: "))
NumWidgetsFri = int(input("Enter number of widgets produced on Friday: "))

# Calculations
RegularPay = HoursWorked * HOURLY_PAY_RATE
TotWeeklyWidgets = NumWidgetsMon + NumWidgetsTues + NumWidgetsWed + NumWidgetsThurs + NumWidgetsFri
Commission = TotWeeklyWidgets * COMMISSION_RATE
GrossPay = RegularPay + Commission

IncomeTaxOwed = GrossPay * INCOME_TAX_RATE
CPP_Owed = GrossPay * CPP_RATE
EI_Owed = GrossPay * EI_RATE                                                                                # Old MacDonald had a farm. EI_Owed.
TotDeductions = IncomeTaxOwed + CPP_Owed + EI_Owed + UNION_DUES
NetPay = GrossPay - TotDeductions

# Print input:
print()
print("Employee's name: ", EmployeeName)
print("Total number of widgets produced: ", TotWeeklyWidgets)
print()

# Print calculated values to the user:
print(f"Regular pay: ${RegularPay:,.2f}")
print(f"Commission: ${Commission:,.2f}")
print(f"Gross pay: ${GrossPay:,.2f}")
print(f"Income tax: ${IncomeTaxOwed:,.2f}")
print(f"CPP: ${CPP_Owed:,.2f}")
print(f"EI: ${EI_Owed:,.2f}")
print(f"Union Dues: ${UNION_DUES}")
print(f"Total deductions: ${TotDeductions:,.2f}")
print(f"Net pay: ${NetPay:,.2f}")


