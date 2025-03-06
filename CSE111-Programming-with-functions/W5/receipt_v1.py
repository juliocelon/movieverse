import csv

def main():

    PRODUCT_NUMBER = 0
    PRODUCT_NAME = 1
    PRODUCT_PRICE = 2

    PRODUCT_QUANTITY = 1

    products_dict = read_dictionary("products.csv", PRODUCT_NUMBER)
    print(products_dict)

    with open("request.csv", "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)
        print("Requested Items")
        for line in reader:
            if len(line) != 0:
                if line[PRODUCT_NUMBER] in products_dict:
                    product = products_dict[line[PRODUCT_NUMBER]]
                    print(f"{product[PRODUCT_NAME]}: "
                          f"{line[PRODUCT_QUANTITY]} @ {product[PRODUCT_PRICE]}")

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