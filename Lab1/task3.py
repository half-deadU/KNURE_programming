sales = [
    {"item_name": "яблуко", "item_quantity": 20, "item_price": 5},
    {"item_name": "банан", "item_quantity": 10, "item_price": 3},
    {"item_name": "не яблуко", "item_quantity": 50, "item_price": 20.2},
    {"item_name": "вишня", "item_quantity": 100, "item_price": 12}
]

def calculate_revenue(sales):
    revenue = {}
    for sale in sales:
        item_name = sale["item_name"]
        total_revenue = sale["item_quantity"] * sale["item_price"]
        revenue[item_name] = revenue.get(item_name, 0) + total_revenue
    return revenue

revenue = calculate_revenue(sales)
frequent_items = [item for item, total in revenue.items() if total > 1000]

print("Дохід за продуктами:", revenue)
print("Продукти з доходом > 1000:", frequent_items)
