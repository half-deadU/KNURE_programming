def analyze_log_file(log_file_path):
    response_codes = {}

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) >= 9:
                    status_code = parts[8]
                    if status_code.isdigit():
                        response_codes[status_code] = response_codes.get(status_code, 0) + 1

    except FileNotFoundError:
        print(f"Помилка: файл '{log_file_path}' не знайдено.")
    except IOError:
        print(f"Помилка: не вдалося прочитати файл '{log_file_path}'.")

    return response_codes

if __name__ == "__main__":
    path = input("Введіть шлях до лог-файлу: ").strip()
    result = analyze_log_file(path)

    if result:
        print("\nСтатистика кодів відповіді HTTP:")
        for code, count in sorted(result.items()):
            print(f"Код {code}: {count}")

"""C:\nya_local\apache_logs.txt"""