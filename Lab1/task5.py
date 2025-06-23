import hashlib

user_db = {
    "ivan123": {
        "password": hashlib.md5("qwerty123".encode()).hexdigest(),
        "full_name": "Ярослав Скубіш Ігорович"
    },
    "maria456": {
        "password": hashlib.md5("12345".encode()).hexdigest(),
        "full_name": "Олег Скиба Олегович"
    },
    "oleg789": {
        "password": hashlib.md5("password789".encode()).hexdigest(),
        "full_name": "Ярослав Квадрат Ярославович"
    }
}

def check_login():
    username = input("Введіть логін: ")
    if username in user_db:
        password_input = input("Введіть пароль: ")
        hashed = hashlib.md5(password_input.encode()).hexdigest()
        if hashed == user_db[username]["password"]:
            print("Доступ дозволено:", user_db[username]["full_name"])
        else:
            print("Невірний пароль.")
    else:
        print("Користувача не знайдено.")

check_login()
