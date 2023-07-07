# Program description: a program to help Honest Harry keep track of sales at his used car lot.
# Written by: Evan Harte
# Date: Jun 7, 2023

import datetime


# Constants:
INVOICE_DATE = datetime.datetime.now()
InvDate = datetime.datetime.strftime(INVOICE_DATE, "%B %d, %Y")
LICENSE_FEE_RATE1 = 75.00
LICENSE_FEE_RATE2 = 165.00
TRANSFER_FEE_RATE = .01
LUXURY_TAX_RATE = .016
HST_RATE = .15
FINANCE_FEE = 39.99


# Extra variables / literals - the directions didn't specify these for input so I put them here.
STREET_ADDRESS = "123 Python Blvd."
CITY = "St. John's"
PROVINCE = "NL"
POSTAL_CODE = "A1A1A1"


# Inputs / validations:
while True:

    while True:
        print()
        CustFirstName = input("Enter first name ('END' to quit): ")
        if CustFirstName == "":
            print("Error - First name cannot be blank.")
        elif CustFirstName == "END":
            quit()
        else:
            CustFirstName = CustFirstName.title()
            break

    while True:
        CustLastName = input("Enter last name: ").title()
        if CustLastName == "":
            print("Error - Last name cannot be blank.")
        else:
            break

    while True:
        PhNum = input("Enter phone number (9999999999): ")
        if PhNum == "":
            print("Error - Phone number cannot be blank.")
        elif len(PhNum) != 10:
            print("Error - Phone number must be 10 digits (9999999999).")
        elif not PhNum.isdigit():
            print("Error - phone number must contain only numbers.")
        else:
            break

    while True:
        PlateNum = input("Enter license plate number (XXX999): ").upper()
        if PlateNum == "":
            print("Error - License plate number cannot be blank.")
        elif len(PlateNum) != 6:
            print("Error - License plate number must be 6 characters.")
        elif not PlateNum[0:3].isalpha():
            print("Error - First three characters of license plate must be letters.")
        elif not PlateNum[3:].isdigit():
            print("Error - Last three characters of license plate must be numbers.")
        else:
            break

    while True:
        CarMake = input("Enter the car make (ie. Toyota): ").title()
        if CarMake == "":
            print("Error - Car make cannot be blank.")
        else:
            break

    while True:
        CarModel = input("Enter the car model (ie. Corolla): ").title()
        if CarModel == "":
            print("Error - Car model cannot be blank.")
        else:
            break

    while True:
        CarYear = input("Enter car year (ie. 2018): ")
        if CarYear == "":
            print("Error - Car year cannot be blank.")
        elif not CarYear.isdigit():
            print("Error - Car year must contain only numbers.")
        elif len(CarYear) != 4:
            print("Error - Car year must be 4 numbers (ie. 2018).")
        else:
            break

    while True:
        try:
            SellingPrice = float(input("Enter the selling price: $"))
        except:
            print("Error - invalid input. Must be a valid number.")
        else:
            if SellingPrice < 0:
                print("Error - Selling price cannot be a negative number.")
            elif SellingPrice > 50000.00:
                print("Error - Selling price cannot exceed $50,000.00.")
            else:
                break

    while True:
        try:
            TradePrice = float(input("Enter the amount of the trade-in: $"))
        except:
            print("Error - invalid input. Must be a valid number.")
        else:
            if TradePrice < 0:
                print("Error - Trade-in price cannot be a negative number.")
            elif TradePrice > SellingPrice:
                print("Error - Trade-in price cannot exceed the selling price.")
            else:
                break

    while True:
        SalespersonName = input("Enter the salesperson's name: ").title()
        if SalespersonName == "":
            print("Error - Salesperson's name cannot be blank.")
        else:
            break

    # Calculations:

    PriceAftTrade = SellingPrice - TradePrice

    if SellingPrice <= 5000.00:
        LicenseFee = LICENSE_FEE_RATE1
    else:
        LicenseFee = LICENSE_FEE_RATE2

    TransferFee = SellingPrice * TRANSFER_FEE_RATE
    if SellingPrice > 20000.00:
        LuxTax = SellingPrice * LUXURY_TAX_RATE
        TransferFee += LuxTax
    else:
        LuxTax = 0

    SubTotal = PriceAftTrade + LicenseFee + TransferFee
    HST = SubTotal * HST_RATE
    TotSalesPrice = SubTotal + HST


    # Display / output:

    print()
    print(f"Honest Harry Car Sales                        Invoice Date:   {InvDate}")
    CustInitials = f"{CustFirstName[0] + CustLastName[0]}"
    PlateNumLast3 = PlateNum[3:]
    PhNumLast4 = PhNum[6:]
    print(f"Used Car Sale and Receipt                     Receipt No:       {CustInitials}-{PlateNumLast3}-{PhNumLast4}")
    print()
    SellingPriceDSP = f"${SellingPrice:,.2f}"
    print(" "*40, f"Sale price:             {SellingPriceDSP:>10s}")
    TradePriceDSP = f"${TradePrice:,.2f}"
    print("Sold to:", " "*31, f"Trade Allowance:        {TradePriceDSP:>10s}")
    print(" "*40, "-"*34)

    PriceAftTradeDSP = f"${PriceAftTrade:,.2f}"
    print(f"     {CustFirstName[0]}. {CustLastName:<26s}       Price after Trade:      {PriceAftTradeDSP:>10s}")
    LicenseFeeDSP = f"${LicenseFee:,.2f}"
    print(f"     {STREET_ADDRESS:<29s}       License Fee:            {LicenseFeeDSP:>10s}")
    TransferFeeDSP = f"${TransferFee:,.2f}"
    print(f"     {CITY:<19s},{PROVINCE} {POSTAL_CODE}       Transfer Fee:           {TransferFeeDSP:>10s}")
    print(" " * 40, "-" * 34)

    SubTotalDSP = f"${SubTotal:,.2f}"
    print("Car Details:", " "*27, f"Subtotal:               {SubTotalDSP:>10s}")
    HST_DSP = f"${HST:,.2f}"
    print(" " * 40, f"HST:                    {HST_DSP:>10s}")
    print(f"     {CarYear} {CarMake:<13s} {CarModel:<10s}       ----------------------------------")
    TotSalesPriceDSP = f"${TotSalesPrice:,.2f}"
    print(" " * 40, f"Total sales price:      {TotSalesPriceDSP:>10s}")
    print("-" * 75)
    print("                    Best used cars at the best prices!")
    print()

    # Payment schedule display:

    print()
    print("                              Financing     Total        Monthly")
    print("    # Years    # Payments        Fee        Price        Payment")
    print("    ------------------------------------------------------------")

    for Years in range(1, 5):
        Payments = Years * 12
        FinancingFee = Years * FINANCE_FEE
        FinancingFeeDSP = f"${FinancingFee:,.2f}"
        TotPrice = TotSalesPrice + FinancingFee
        TotPriceDSP = f"${TotPrice:,.2f}"
        MonthlyPay = TotPrice / Payments
        MonthlyPayDSP = f"${MonthlyPay:,.2f}"

        print(f"       {Years}           {Payments}          {FinancingFeeDSP:>7s}    {TotPriceDSP:>10s}   {MonthlyPayDSP:>9s}")

    InvMON = datetime.datetime.strftime(INVOICE_DATE, "%b")
    InvMON = str(InvMON).upper()
    InvDay = INVOICE_DATE.day
    InvYear = INVOICE_DATE.year
    print("    ------------------------------------------------------------")
    FirstPayDate = INVOICE_DATE + datetime.timedelta(days=30)
    FirstPayMON = datetime.datetime.strftime(FirstPayDate, "%b")
    FirstPayMON = str(FirstPayMON).upper()
    FirstPayDay = FirstPayDate.day
    FirstPayYear = FirstPayDate.year

    print(f"    Invoice date: {InvDay}-{InvMON}-{InvYear}      First payment date: {FirstPayDay}-{FirstPayMON}-{FirstPayYear}")
