inventory = {
    "яблука": 10,
    "банани": 3,
    "молоко": 2,
    "хліб": 6
}

def update_inventory(product, quantity):
    inventory[product] = inventory.get(product, 0) + quantity
    if inventory[product] < 0:
        inventory[product] = 0

low_stock = [product for product, qty in inventory.items() if qty < 5]

while True:
    print("\nПоточний інвентар:", inventory)
    print("Продукти з кількістю менше 5:", low_stock)
    action = input("Введіть дію (додати/видалити/вийти): ").strip().lower()

    if action == "вийти":
        break
    elif action in ("додати", "видалити"):
        product = input("Введіть назву продукту: ").strip().lower()
        try:
            amount = int(input("Введіть кількість: "))
        except ValueError:
            print("Кількість повинна бути числом.")
            continue

        if action == "видалити":
            amount = -amount

        update_inventory(product, amount)
    else:
        print("Невідома дія. Введіть 'додати', 'видалити' або 'вийти'.")

print("\nФінальний інвентар:", inventory)
print("Продукти з кількістю менше 5:", low_stock)
