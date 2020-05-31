

base_restaurant_bill = float(input("How much was the bill without tax or tip?"))
sales_tax = float(input("What is the percentage sales tax rate?")) / 100
rating_of_service = int(input("How would you rate the service, on a scale of 1 to 10?"))
number_of_payers = int(input("How many people will contribute to payment?"))

def calculate_bill_with_tax_for_each():
    tax_total = base_restaurant_bill * sales_tax
    total_bill_with_tax = base_restaurant_bill + tax_total
    bill_with_tax_for_each = total_bill_with_tax / number_of_payers
    return bill_with_tax_for_each

def convert_rating_to_tip_percentage(service_rating):
    if (rating_of_service == 0):
        tip_percentage = 0
    elif (rating_of_service == 1):
        tip_percentage = 0.03
    elif (rating_of_service == 2):
        tip_percentage = 0.06
    elif (rating_of_service == 3):
        tip_percentage = 0.09
    elif (rating_of_service == 4):
        tip_percentage = 0.12
    elif (rating_of_service == 5):
        tip_percentage = 0.15
    elif (rating_of_service == 6):
        tip_percentage = 0.18
    elif (rating_of_service == 7):
        tip_percentage = 0.21
    elif (rating_of_service == 8):
        tip_percentage = 0.24
    elif (rating_of_service == 9):
        tip_percentage = 0.27
    else:
        tip_percentage = 0.30
    return tip_percentage

def calculate_amount_of_tip_to_pay_for_each():
    tip_total = base_restaurant_bill * convert_rating_to_tip_percentage(rating_of_service)
    tip_per_person_amount = tip_total / number_of_payers
    return tip_per_person_amount

def caculate_total_bill_with_tax_and_tip_for_each(total_for_everything):
    total_bill_per_person = calculate_total_bill_with_tax_and_tip_for_all() / number_of_payers
    return total_bill_per_person

def calculate_total_bill_with_tax_and_tip_for_all():
    tax_total = base_restaurant_bill * sales_tax
    total_bill_with_tax = base_restaurant_bill + tax_total
    tip_total = base_restaurant_bill * convert_rating_to_tip_percentage(rating_of_service)
    total_bill_for_everyone = total_bill_with_tax + tip_total
    return total_bill_for_everyone

# def calculate_total_bill_with_tax_and_tip_for_all():
#     total_bill_for_everyone = (calculate_bill_with_tax_for_each() * number_of_payers) + (calculate_amount_of_tip_to_pay_for_each() * number_of_payers)
#     print("oldcalc " + str(total_bill_for_everyone))
#     return total_bill_for_everyone


print("Total bill per person with tax: $" + str(calculate_bill_with_tax_for_each()) + ".")
print("Tip per person: $" + str(round(calculate_amount_of_tip_to_pay_for_each(),2)) + ".")
print("Total per person including tax and tip: $" + str(round(caculate_total_bill_with_tax_and_tip_for_each(calculate_total_bill_with_tax_and_tip_for_all()),2)) + ".")
print("Total bill including tax and tip: $" + str(calculate_total_bill_with_tax_and_tip_for_all()) + ".")