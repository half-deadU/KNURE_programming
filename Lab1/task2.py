stock = {
    "яблука": 10,
    "банани": 3,
    "молоко": 2,
    "хліб": 6
}

def update_stock(item_name, item_quantity):
    stock[item_name] = stock.get(item_name, 0) + item_quantity
    if stock[item_name] < 0:
        stock[item_name] = 0

while True:
    low_stock = [item for item, qty in stock.items() if qty < 5]
    print("\nПоточний інвентар:", stock)
    print("Продукти з кількістю менше 5:", low_stock)
    action = input("Введіть дію (додати/видалити/вийти): ").strip().lower()

    if action == "вийти":
        break
    elif action in ("додати", "видалити"):
        item_name = input("Введіть назву продукту: ").strip().lower()
        try:
            item_quantity = int(input("Введіть кількість: "))
        except ValueError:
            print("Кількість повинна бути числом.")
            continue

        if action == "видалити":
            item_quantity = -item_quantity

        update_stock(item_name, item_quantity)
    else:
        print("Невідома дія.")

print("\nФінальний інвентар:", stock)
print("Продукти з кількістю менше 5:", low_stock)
