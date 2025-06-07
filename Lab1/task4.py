tasks = {
    "Зробити лабораторну": "в процесі",
    "Завантажити дані": "очікує",
    "Забути на пів-року": "виконано"
}

def update_task(name, new_status):
    tasks[name] = new_status

def remove_task(name):
    if name in tasks:
        del tasks[name]

while True:
    pending_tasks = [task for task, status in tasks.items() if status == "очікує"]

    print("\nПоточні задачі:")
    for name, status in tasks.items():
        print(f" - {name}: {status}")
    print("Задачі зі статусом 'очікує':", pending_tasks)

    action = input("\nВведіть дію (додати/видалити/змінити/вийти): ").strip().lower()

    if action == "вийти":
        break
    elif action == "додати":
        name = input("Введіть назву нової задачі: ").strip()
        status = input("Введіть статус (очікує / в процесі / виконано): ").strip().lower()
        if status not in ["очікує", "в процесі", "виконано"]:
            print("Недійсний статус. Використано 'очікує' за замовчуванням.")
            status = "очікує"
        update_task(name, status)
    elif action == "видалити":
        name = input("Введіть назву задачі для видалення: ").strip()
        if name in tasks:
            remove_task(name)
        else:
            print("Задачу не знайдено.")
    elif action == "змінити":
        name = input("Введіть назву задачі для зміни статусу: ").strip()
        if name in tasks:
            new_status = input("Введіть новий статус (очікує / в процесі / виконано): ").strip().lower()
            if new_status in ["очікує", "в процесі", "виконано"]:
                update_task(name, new_status)
            else:
                print("Недійсний статус.")
        else:
            print("Задачу не знайдено.")
    else:
        print("Невідома дія. Введіть 'додати', 'видалити', 'змінити' або 'вийти'.")

print("\nФінальний список задач:")
for name, status in tasks.items():
    print(f" - {name}: {status}")
print("Задачі зі статусом 'очікує':", pending_tasks)