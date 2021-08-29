import os
import datetime

'''Intermediate Variable file name which can be edited as needed '''

# Assign current date to a variable
today_date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')

file_name = 'vm_data.csv'
product_price = 0.50
temp_file = 'temp.csv'

# Selection button image filename
coke = 'coke.png'
fanta = 'fanta.png'
sprite = 'sprite.png'
water = 'water.png'

# Function to return path of filename
# update below path based on the image file and the csv file location
def database_file(filename):
    return os.path.join('C:', os.sep, 'Users', 'Nvidia', 'Desktop', 'projects', 'VendingMachineProgram', 'icon', filename)

def remove_file():
    os.remove(database_file(temp_file))

