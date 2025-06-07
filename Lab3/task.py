import sqlite3
import hashlib

DATABASE_NAME = 'users.db'

def initialize_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            login TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            full_name TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Базу даних '{DATABASE_NAME}' та таблицю 'users' ініціалізовано.")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(login, password, full_name):
    hashed_password = hash_password(password)
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)",
                       (login, hashed_password, full_name))
        conn.commit()
        print(f"Користувача '{login}' успішно додано.")
    except sqlite3.IntegrityError:
        print(f"Помилка: Користувач з логіном '{login}' вже існує.")
    finally:
        conn.close()

def update_password(login, new_password):
    hashed_new_password = hash_password(new_password)
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = ? WHERE login = ?",
                   (hashed_new_password, login))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Пароль для користувача '{login}' успішно оновлено.")
    else:
        print(f"Помилка: Користувача з логіном '{login}' не знайдено.")
    conn.close()

def authenticate_user(login, entered_password):
    hashed_entered_password = hash_password(entered_password)
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE login = ?", (login,))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_hashed_password = result[0]
        if hashed_entered_password == stored_hashed_password:
            print(f"Автентифікація для користувача '{login}' успішна.")
            return True
        else:
            print(f"Автентифікація для користувача '{login}' не вдалася: невірний пароль.")
            return False
    else:
        print(f"Автентифікація для користувача '{login}' не вдалася: користувача не знайдено.")
        return False

if __name__ == "__main__":
    initialize_database()

    while True:
        print("\n--- Меню ---")
        print("1. Додати нового користувача")
        print("2. Оновити пароль користувача")
        print("3. Перевірити автентифікацію користувача")
        print("4. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            login = input("Введіть логін нового користувача: ")
            password = input("Введіть пароль: ")
            full_name = input("Введіть повне ім'я (ПІБ): ")
            add_user(login, password, full_name)
        elif choice == '2':
            login = input("Введіть логін користувача, чий пароль потрібно оновити: ")
            new_password = input("Введіть новий пароль: ")
            update_password(login, new_password)
        elif choice == '3':
            login = input("Введіть логін користувача для автентифікації: ")
            entered_password = input("Введіть пароль: ")
            authenticate_user(login, entered_password)
        elif choice == '4':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")