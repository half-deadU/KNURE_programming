import hashlib

users = {
    "ivan123": {
        "password": hashlib.md5("qwerty123".encode()).hexdigest(),
        "full_name": "Іван Іванович Іваненко"
    },
    "maria456": {
        "password": hashlib.md5("12345".encode()).hexdigest(),
        "full_name": "Марія Петрівна Коваль"
    },
    "oleg789": {
        "password": hashlib.md5("password789".encode()).hexdigest(),
        "full_name": "Олег Миколайович Сидорчук"
    }
}

def check_login():
    login = input("Введіть логін: ")
    if login in users:
        password = input("Введіть пароль: ")
        hashed = hashlib.md5(password.encode()).hexdigest()
        if hashed == users[login]["password"]:
            print("Доступ дозволено:", users[login]["full_name"])
        else:
            print("Невірний пароль.")
    else:
        print("Користувача не знайдено.")

check_login()
