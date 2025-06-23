def analyze_log_file(input_path):
    results = {}

    try:
        with open(input_path, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) >= 9:
                    status_code = parts[8]
                    if status_code.isdigit():
                        results[status_code] = results.get(status_code, 0) + 1

    except FileNotFoundError:
        print(f"Помилка: файл '{input_path}' не знайдено.")
    except IOError:
        print(f"Помилка: не вдалося прочитати файл '{input_path}'.")

    return results

if __name__ == "__main__":
    input_path = input("Введіть шлях до лог-файлу: ").strip()
    results = analyze_log_file(input_path)

    if results:
        print("\nСтатистика кодів відповіді HTTP:")
        for code, count in sorted(results.items()):
            print(f"Код {code}: {count}")

"""C:\nya_local\apache_logs.txt"""
