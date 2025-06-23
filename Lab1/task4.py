task_list = {
    "Зробити лабораторну": "в процесі",
    "Завантажити дані": "очікує",
    "Забути на пів-року": "виконано"
}

def update_task(task_name, task_status):
    task_list[task_name] = task_status

def remove_task(task_name):
    if task_name in task_list:
        del task_list[task_name]

while True:
    pending_tasks = [t for t, s in task_list.items() if s == "очікує"]

    print("\nПоточні задачі:")
    for task_name, task_status in task_list.items():
        print(f" - {task_name}: {task_status}")
    print("Задачі зі статусом 'очікує':", pending_tasks)

    action = input("\nВведіть дію (додати/видалити/змінити/вийти): ").strip().lower()

    if action == "вийти":
        break
    elif action == "додати":
        task_name = input("Введіть назву нової задачі: ").strip()
        task_status = input("Введіть статус: ").strip().lower()
        if task_status not in ["очікує", "в процесі", "виконано"]:
            task_status = "очікує"
        update_task(task_name, task_status)
    elif action == "видалити":
        task_name = input("Введіть назву задачі для видалення: ").strip()
        remove_task(task_name)
    elif action == "змінити":
        task_name = input("Введіть назву задачі: ").strip()
        if task_name in task_list:
            task_status = input("Введіть новий статус: ").strip().lower()
            if task_status in ["очікує", "в процесі", "виконано"]:
                update_task(task_name, task_status)
    else:
        print("Невідома дія.")

print("\nФінальний список задач:")
for task_name, task_status in task_list.items():
    print(f" - {task_name}: {task_status}")
print("Задачі зі статусом 'очікує':", pending_tasks)
