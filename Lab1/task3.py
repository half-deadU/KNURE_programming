sales = [
    {"продукт": "яблуко", "кількість": 20, "ціна": 5},
    {"продукт": "банан", "кількість": 10, "ціна": 3},
    {"продукт": "не яблуко", "кількість": 50, "ціна": 20.2},
    {"продукт": "вишня", "кількість": 100, "ціна": 12}
]

def calculate_income(sales):
    income = {}
    for sale in sales:
        product = sale["продукт"]
        total = sale["кількість"] * sale["ціна"]
        income[product] = income.get(product, 0) + total
    return income

income_per_product = calculate_income(sales)
high_income_products = [product for product, total in income_per_product.items() if total > 1000]

print("Дохід за продуктами:", income_per_product)
print("Продукти з доходом > 1000:", high_income_products)
