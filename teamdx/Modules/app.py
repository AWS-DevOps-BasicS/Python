print('This is app started')
import sales
import os
import sys
# sys.path will give the list of paths where python will check for modules if the app.py will run 
sys.path.append("F:\\")
import purchase
purchase.create_supplier()
sales.add_customer()
print(sales.a)
print("This is app end")