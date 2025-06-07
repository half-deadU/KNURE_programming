import hashlib

class User:
    def __init__(self, username: str, password: str, is_active: bool = True):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.is_active = is_active

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password: str) -> bool:
        return self.password_hash == self._hash_password(password)

class Administrator(User):
    def __init__(self, username: str, password: str, is_active: bool = True, permissions=None):
        super().__init__(username, password, is_active)
        self.permissions = permissions if permissions is not None else []

    def add_permission(self, permission: str):
        if permission not in self.permissions:
            self.permissions.append(permission)

    def remove_permission(self, permission: str):
        if permission in self.permissions:
            self.permissions.remove(permission)

class RegularUser(User):
    def __init__(self, username: str, password: str, is_active: bool = True):
        super().__init__(username, password, is_active)

class GuestUser(User):
    def __init__(self, username: str):
        super().__init__(username, password='', is_active=True)

    def verify_password(self, password: str) -> bool:
        return False

class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user: User):
        self.users[user.username] = user

    def authenticate_user(self, username: str, password: str) -> User | None:
        user = self.users.get(username)
        if user and user.is_active and user.verify_password(password):
            return user
        return None

def main():
    ac = AccessControl()

    admin = Administrator("admin1", "securepassword", permissions=['add_user', 'delete_user'])
    user = RegularUser("user1", "userpass")
    guest = GuestUser("guest1")

    ac.add_user(admin)
    ac.add_user(user)
    ac.add_user(guest)

    while True:
        print("\nВведіть дані для аутентифікації (або 'exit' щоб вийти):")
        username = input("Ім'я користувача: ")
        if username.lower() == 'exit':
            break
        password = input("Пароль: ")

        user = ac.authenticate_user(username, password)
        if user:
            print(f"Користувач '{user.username}' аутентифікований.")
            if isinstance(user, Administrator):
                print(f"Роль: Адміністратор. Дозволи: {user.permissions}")
            elif isinstance(user, RegularUser):
                print(f"Роль: Звичайний користувач.")
            elif isinstance(user, GuestUser):
                print(f"Роль: Гість.")
        else:
            print("Аутентифікація не пройдена, спробуйте ще раз.")

if __name__ == "__main__":
    main()
