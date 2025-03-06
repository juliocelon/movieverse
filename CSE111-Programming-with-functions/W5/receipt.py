
"""
Author: Julio Celón
Title: W05 Project: Grocery Store

NOTE: Exceeding the Requirements applied:
- Challenge: Write code that will give a buy one, get one half off discount for 
  item D083. 
  For example if the customer orders one item it will be full price. 
  If the customer orders two items the first item is full price the second one 
  is discounted 50%. For three items two would be at full price and one at 50% off. 
  Indicate the discounted price on the receipt.

- Write code to print a reminder of how many days until the New Years Sale 
  begins (Jan 1) at the bottom of the receipt.

"""
import csv
from datetime import datetime

def main():

    PRODUCT_NUMBER = 0
    PRODUCT_NAME = 1
    PRODUCT_PRICE = 2

    PRODUCT_QUANTITY = 1

    PRODUCT_NUMBER_PROMOTION = "D083"
    promotion_applied = False
    discount = 0

    STORE_NAME = "Smart Store"
    try:
        products_dict = read_dictionary("products.csv", PRODUCT_NUMBER)
        print(products_dict)

        REQUEST_FILE = "request.csv"
        with open(REQUEST_FILE, "rt") as csv_file:

            reader = csv.reader(csv_file)
            next(reader)

            print(STORE_NAME)

            number_items = 0
            subtotal = 0.0

            print("Requested Items")
            for line in reader:
                if len(line) != 0:
                    
                    # Change in indentation and comment to test the exception
                    #if line[PRODUCT_NUMBER] in products_dict:

                    product_number = line[PRODUCT_NUMBER]

                    product = products_dict[product_number]
                        
                    name = product[PRODUCT_NAME]
                    price = product[PRODUCT_PRICE]
                    quantity = int(line[PRODUCT_QUANTITY])

                    if product_number == PRODUCT_NUMBER_PROMOTION and \
                    quantity > 1 and promotion_applied == False:
                        discount = float(price) * 0.50
                        total_price = float(quantity) * float(price) - \
                                    discount
                        subtotal += total_price
                        promotion_applied = True

                    else:
                        subtotal += quantity * float(price)

                    number_items += quantity
                    
                    print(f"{name}: {quantity} @ {price}")

            print(f"Number of Items: {number_items}")
            print(f"Subtotal: {subtotal:.2f}")

            print(f"Discount: {discount}")

            sales_tax = subtotal * 0.06
            print(f"Sales Tax: {sales_tax:.2f}")

            total = subtotal + sales_tax
            print(f"Total: {total:.2f}")

            print(f"Thank you for shopping at the {STORE_NAME}.")
            
            today = datetime.now()
            print(today.strftime("%a %b %d %H:%M:%S %Y"))

            new_year_sale = datetime(today.year + 1, 1, 1) # Jan 1st of the next year 
            days_remaining = (new_year_sale - today).days
            print("----------------------------")
            print(f"Reminder: Only {days_remaining} days until the New Year's Sale!")
            print("----------------------------")


    except KeyError as key_err:
        print()
        print(f"Error: Unknown product ID in the {REQUEST_FILE} file")
        print(type(key_err).__name__, key_err)

    except FileNotFoundError as not_found_err:
        print()
        print(f"Error: missing file")
        print(type(not_found_err).__name__, not_found_err)
        
def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """
  dictionary = {}

  with open(filename, "rt") as csv_file:

    reader = csv.reader(csv_file)
    next(reader)

    for line in reader:
        if len(line) != 0:
            key = line[key_column_index]
            dictionary[key] = line
  return dictionary

if __name__ == "__main__":
    main()