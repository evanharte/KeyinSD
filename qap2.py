# Description: This program is for the St. John's Marina & Yacht Club to keep track of who has their yachts
# docked, how much to charge them each month, and if the members have paid their bills.

# Written by: Evan Harte
# Date written: May 25, 2023

# Constants:
EVEN_SITE_RATE = 80.00
ODD_SITE_RATE = 120.00
ALT_MEMB_RATE = 5.00
SITE_CLEAN_FEE = 50.00
VID_SURVEIL_FEE = 35.00
HST_RATE = .15
PROCESS_FEE = 59.99
CANCEL_RATE = .60
DATE = "2023-05-27"

# Inputs:
SiteNum = int(input("Enter the site number: "))
MembName = input("Enter the member name: ")
StrAdd = input("Enter street address: ")
City = input("Enter city: ")
Province = input("Enter province (eg. NL, NB, ON...): ").upper()
PostCode = input("Enter the postal code (eg. A1A1A1): ")
PhNumHome = input("Enter home phone number (eg. 7095551234): ")
PhNumCell = input("Enter cell phone number (eg. 7095556789): ")
MembType = input("Enter the membership type ('S' for standard or 'E' for executive): ").upper()
NumAltFamMembs = int(input("Enter the number of alternate family members: "))
SiteCleaning = input("Weekly site cleaning? (Y/N): ").upper()
VidSurveil = input("Video surveillance? (Y/N): ").upper()

# Calculations:
if SiteNum % 2 == 0:
    SiteCharges = EVEN_SITE_RATE + (NumAltFamMembs * ALT_MEMB_RATE)
else:
    SiteCharges = ODD_SITE_RATE + (NumAltFamMembs * ALT_MEMB_RATE)


if (SiteCleaning == "Y") and (VidSurveil == "Y"):
    ExtraCharges = SITE_CLEAN_FEE + VID_SURVEIL_FEE
elif (SiteCleaning == "Y") and (VidSurveil == "N"):
    ExtraCharges = SITE_CLEAN_FEE
elif (SiteCleaning == "N") and (VidSurveil == "Y"):
    ExtraCharges = VID_SURVEIL_FEE
else:
    ExtraCharges = 0

SubTotal = SiteCharges + ExtraCharges
HST = SubTotal * HST_RATE
TotMonthCharge = SubTotal + HST

if MembType == "E":
    MonthlyDues = 150.00
else:
    MonthlyDues = 75.00

TotMonthFees = TotMonthCharge + MonthlyDues

TotYearFees = TotMonthFees * 12
MonthlyPayment = (TotYearFees + PROCESS_FEE) / 12

CancelFee = (SiteCharges * 12) * CANCEL_RATE


# Display:
print()
print("  St. John's Marina & Yacht Club")
print("       Yearly Member Receipt")
print()
print("-----------------------------------")
print()
print("Client Name and Address:")
print()
print(f"{MembName:<24s}")
print(f"{StrAdd:<24s}")
print(f"{City:<15s}, {Province:<2s} {PostCode:<6s}")
print()
print(f"Phone: {PhNumHome:<10s} (H)")
print(f"       {PhNumCell:<10s} (C)")
print()
MembTypeE = "Executive"
MembTypeS = "Standard"
if MembType == "E":
    print(f"Site #: {SiteNum:<3d} Member type: {MembTypeE:<9s}")
else:
    print(f"Site #: {SiteNum:<3d} Member type: {MembTypeS:<9s}")

print()
print(f"Alternate members:              {NumAltFamMembs:>2d}")
SiteCleaningY = "Yes"
SiteCleaningN = "No"
VidSurveilY = "Yes"
VidSurveilN = "No"
if SiteCleaning == "Y":
    print(f"Weekly site cleaning:          {SiteCleaningY:>3s}")
else:
    print(f"Weekly site cleaning:          {SiteCleaningN:>3s}")

if VidSurveil == "Y":
    print(f"Video surveillance:            {VidSurveilY:>3s}")
else:
    print(f"Video surveillance:            {VidSurveilN:>3s}")

print()
SiteChargesDSP = f"${SiteCharges:,.2f}"
print(f"Site charges:            {SiteChargesDSP:>9s}")
ExtraChargesDSP = f"${ExtraCharges:,.2f}"
print(f"Extra charges:             {ExtraChargesDSP:>7s}")
print("                        -----------")
SubTotalDSP = f"${SubTotal:,.2f}"
print(f"Subtotal:                {SubTotalDSP:>9s}")
HST_DSP = f"${HST:,.2f}"
print(f"Sales tax (HST):           {HST_DSP:>7s}")
print("                        -----------")
TotMonthChargeDSP = f"${TotMonthCharge:,.2f}"
print(f"Total monthly charges:   {TotMonthChargeDSP:>9s}")
MonthlyDuesDSP = f"${MonthlyDues:,.2f}"
print(f"Monthly dues:              {MonthlyDuesDSP:>7s}")
print("                        -----------")
TotMonthFeesDSP = f"${TotMonthFees:,.2f}"
print(f"Total monthly fees:      {TotMonthFeesDSP:>9s}")
TotYearFeesDSP = f"${TotYearFees:,.2f}"
print(f"Total yearly fees:      {TotYearFeesDSP:>10s}")
print()
MonthlyPaymentDSP = f"${MonthlyPayment:,.2f}"
print(f"Monthly payment:         {MonthlyPaymentDSP:>9s}")
print()
print("-----------------------------------")
print()
print(f"Issued: {DATE}")
print(f"HST Reg No: 549-33-5849-4720-9885")
print()
CancelFeeDSP = f"${CancelFee:,.2f}"
print(f"Cancellation fee:        {CancelFeeDSP:>9s}")
print()
