import json
from datetime import datetime, timedelta

def days_between(d1, d2):       
    return abs((d2 - d1).days)

with open('purchases.json') as json_file:
    loaded_json = json.loads(json_file.read())

customer_purchases = loaded_json['customer']['purchases']

# This dict will contain the purchase history of every product, following the next structure:
# key = product name
# value = list of dates when the product was purchased
purchase_history = dict() 

for purchase in customer_purchases:
    date = purchase['date']
    for product in purchase['products']:
        if product['name'] in purchase_history:
            purchase_history[product['name']].append(date)
        else:
            purchase_history[product['name']] = [date]
        

# At this point the purchase_history dictionary is populated
# Now, we will calculate the next purchase date for every product

for product_name, dates in purchase_history.items():
    if (len(dates) >= 2):
        last_two_dates = dates[-2:]
        date_1 = datetime.strptime(last_two_dates[0], '%Y-%d-%m').date()
        date_2 = datetime.strptime(last_two_dates[1], '%Y-%d-%m').date()
        next_purchase = date_2 + timedelta(days=days_between(date_1, date_2))
        print("The next purchase date for " + product_name + " will be on " + next_purchase.strftime('%Y-%d-%m'))
        
