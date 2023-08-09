""" #from shopping.sales import calc_shipping
#from ecommerce.payment import makepayment
from shopping import sales

calc_shipping()
makepayment() 
print(dir(sales))
print(sales.__name__)
print(sales.__package__)
print(sales.__file__) """


from shopping import sales

print(sales.calc_shipping)
