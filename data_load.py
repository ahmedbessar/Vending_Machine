import csv
import os
import input_variable as inp

"""Data load to backend file"""

def data_entry(item_number):
    if item_number == '1':
        product_name = 'coke'
    elif item_number == '2':
        product_name = 'sprite'
    elif item_number == '3':
        product_name = 'fanta'
    else:
        product_name = 'water'

    if os.path.exists(inp.database_file(inp.file_name)):
        with open(inp.database_file(inp.file_name), 'a') as csv_file:
            csv_writer = csv.writer(csv_file, lineterminator = '\n')
            csv_writer.writerow([item_number, product_name, inp.product_price, inp.today_date])
    else:
        with open(inp.database_file(inp.file_name), 'w') as csv_file:
            csv_writer = csv.writer(csv_file, lineterminator = '\n')
            csv_writer.writerow(['Product_ID', 'Product_Name', 'Product_Price', 'Sales_Date'])
            csv_writer.writerow([item_number, product_name, inp.product_price, inp.today_date])