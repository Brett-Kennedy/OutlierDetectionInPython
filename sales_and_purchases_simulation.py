import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt 

class Purchacer:
    def __init__(self, staff_id):
        self.staff_id = staff_id
        
    def consider_purchase(self): #A
        global inventory
        global transactions
        if (current_datetime.hour < 9) or (current_datetime.hour > 17): #B
            return
        if np.random.random() > 0.01: #C
            product_id = np.random.choice(range(num_items_in_inventory))
            if inventory[product_id] > 1000: #D
                return        
            supplier_id = np.random.choice(range(num_suppliers)) #E
            unit_cost = abs(np.random.normal()) * 20.0
            num_purchased = np.random.randint(10, 200)
            total_cost = num_purchased * unit_cost
            inventory[product_id] += num_purchased        
            transactions.append(['Purchase', self.staff_id, supplier_id, product_id, 
                                 current_datetime.strftime("%Y-%m-%d %H:%M"),
                                 num_purchased, unit_cost, total_cost,
                                 inventory[product_id]])

class RoguePurchaser: #F
    def __init__(self, staff_id):
        self.staff_id = staff_id
        self.extra_purchase_months = []
        
    def consider_purchase(self):
        global inventory
        global transactions
        if (current_datetime.hour < 9) or (current_datetime.hour > 17):
            return
        
        if (current_datetime.day == 28) and \
            (current_datetime.month not in self.extra_purchase_months): #G
            product_id = 5
            supplier_id = 10
            unit_cost = abs(np.random.normal()) * 60.0  # 40.0
            #trend_factor = np.log2(current_datetime.month+1) + 1
            trend_factor = current_datetime.month + 1
            num_purchased = int(np.random.randint(50, 60) * trend_factor)  
            #print(current_datetime.month, trend_factor, num_purchased)
            total_cost = num_purchased * unit_cost
            inventory[product_id] += num_purchased        
            transactions.append(['Purchase', self.staff_id, supplier_id, product_id, 
                                 current_datetime.strftime("%Y-%m-%d %H:%M"),
                                 num_purchased, unit_cost, total_cost, 
                                 inventory[product_id]])            
            self.extra_purchase_months.append(current_datetime.month)
        
        elif np.random.random() > 0.01:
            product_id = np.random.choice(range(num_items_in_inventory))
            if product_id == 0: #H
                return            
            if inventory[product_id] > 1000:
                return        
            supplier_id = np.random.choice(range(num_suppliers))
            unit_cost = abs(np.random.normal()) * 20.0
            num_purchased = np.random.randint(10, 200)
            total_cost = num_purchased * unit_cost
            inventory[product_id] += num_purchased        
            transactions.append(['Purchase', self.staff_id, supplier_id, product_id, 
                                 current_datetime.strftime("%Y-%m-%d %H:%M"),
                                 num_purchased, unit_cost, total_cost, 
                                 inventory[product_id]])
            
class Sales: #I
    def consider_sale(self):
        global inventory
        if (current_datetime.hour < 9) or (current_datetime.hour > 17):
            return
        if np.random.random() > 0.8:
            num_sold = np.random.randint(1, 50)
            product_id = np.random.choice(range(num_items_in_inventory))
            if num_sold < inventory[product_id]:
                inventory[product_id] -= num_sold   
                transactions.append(['Sale', 100, -1, product_id, 
                                     current_datetime.strftime("%Y-%m-%d %H:%M"), 
                                     num_sold, -1, -1, inventory[product_id]])
    
    
np.random.seed(0)
    
current_datetime = datetime(2022, 12, 15) 
end_date = datetime(2023, 12, 31)
delta = timedelta(minutes=1)
num_items_in_inventory = 20
inventory = [0]*num_items_in_inventory 
num_purchasers = 10
num_suppliers = 20
list_purchasers = list(range(num_purchasers))

purchasers_arr = [Purchacer(x) for x in range(num_purchasers)]
rogue_purchaser = RoguePurchaser(num_purchasers)
seller = Sales()
transactions = []

while current_datetime <= end_date:       
    np.random.shuffle(list_purchasers)
    for p in list_purchasers:
        purchasers_arr[p].consider_purchase()
    rogue_purchaser.consider_purchase()
    seller.consider_sale()
    
    current_datetime += delta
    
transactions_df = pd.DataFrame(transactions, columns=[
    'Type', 'Staff ID', 'Supplier ID', 'Product ID', 
    'Datetime', 'Count', 'Unit Cost', 'Total Cost', 'Inventory'])
transactions_df = transactions_df[pd.to_datetime(transactions_df['Datetime']) >= datetime(2023, 1, 1)]
#A Simualate a normal purchase agent
#B Only make purchases between 9am and 6pm
#C Randomly decide if will make a purchase
#D Do not buy if there is sufficient in stock
#E Choose a suplier, number bought and unit cost randomly
#F Simulate a rogue process
#G The 28th of each month it makes an unusual purchase
#H This agent does not buy from Supplier 0
#I Simulate a sales process
