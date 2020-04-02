import math
import argparse

# Creating parser
parser = argparse.ArgumentParser()

# adding arguments
parser.add_argument("--type")
parser.add_argument("--principal", type=int, required=False)
parser.add_argument("--periods", type=int, required=False)
parser.add_argument("--interest", type=float, required=False)
parser.add_argument("--payment", type=int)

args = parser.parse_args()
values = vars(args)

Type = values['type']
principal = values['principal']
period = values['periods']
interest = values['interest']
payment = values['payment']

if interest is None or Type is None:
    print("Incorrect parameters")

elif interest < 0:
    print("Incorrect parameters")

elif Type == "annuity":
    interest = interest / (100 * 12)
    # calculate payment
    if principal is not None and period is not None:
        if principal > 0 and period > 0:
            payment = principal * (interest * math.pow(interest + 1, period)) / (math.pow(interest + 1, period) - 1)
            payment = math.ceil(payment)
            overpay = payment * period - principal
            print(f"Your annuity payment = {payment}!")
            print(f"Overpayment = {overpay}")

    # calculate period
    elif principal is not None and payment is not None:
        if principal > 0 and payment > 0:
            months = math.log((payment / (payment - interest * principal)), interest + 1)
            excess = math.ceil(months) - months
            months = math.ceil(months)
            period = months

            year = 0
            while months >= 12:
                year = year + 1
                months = months - 12

            # Generating print_string
            print_string = ""
            if year == 1:
                print_string = " 1 year"
            elif year > 1:
                print_string = f" {year} years"

            if year > 0 and months > 0:
                print_string = print_string + " and "

            if months == 1:
                print_string = print_string + "1 month"
            elif months > 1:
                print_string = print_string + f"{months} months"

            print(f"You need {print_string} to repay this credit!")
            overpay = payment * period - principal
            overpay = math.ceil(overpay)
            print(f"Overpay = {overpay}")

    # calculate principal
    elif period is not None and payment is not None:
        if period > 0 and payment > 0:
            principal = payment / ((interest * math.pow(interest + 1, period)) / (math.pow(interest + 1, period) - 1))
            print(principal)
            overpay = payment * period - principal
            overpay = math.ceil(overpay)
            principal = math.floor(principal)
            print(f"Overpayment = {overpay}")
            print(f"Your credit principal = {principal}!")


    else:
        print("Incorrect parameters")

elif Type == "diff":
    interest = interest / (100 * 12)
    if payment is not None or principal is None or period is None:
        print("Incorrect parameters")

    elif principal > 0 and period > 0:
        tot = 0
        for i in range(period):
            diff = principal / period + interest * (principal - ((principal * i) / period))
            diff = math.ceil(diff)
            tot = tot + diff
            print(f"Month {i + 1}: paid out {diff}")
        overpay = tot - principal
        print(f"\nOverpayment = {overpay}")

    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
