def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = {}

    try:
        with open(input_file_path, 'r') as infile:
            for line in infile:
                ip = line.split()[0] if line.strip() else None
                if ip and ip in allowed_ips:
                    ip_counts[ip] = ip_counts.get(ip, 0) + 1
    except FileNotFoundError:
        print(f"Помилка: вхідний файл '{input_file_path}' не знайдено.")
        return
    except IOError:
        print(f"Помилка: не вдалося прочитати файл '{input_file_path}'.")
        return

    try:
        with open(output_file_path, 'w') as outfile:
            for ip, count in ip_counts.items():
                outfile.write(f"{ip} - {count}\n")
        print(f"Результати записано до файлу '{output_file_path}'.")
    except IOError:
        print(f"Помилка: не вдалося записати до файлу '{output_file_path}'.")

if __name__ == "__main__":
    allowed_ips = [
        "83.149.9.216",
        "110.136.166.128",
        "81.220.24.207"
    ]

    input_path = input("Введіть шлях до вхідного лог-файлу: ").strip()
    output_path = input("Введіть шлях до вихідного файлу для запису результатів: ").strip()

    filter_ips(input_path, output_path, allowed_ips)

"""C:\nya_local\apache_logs.txt"""
"""C:\nya_local\out_log.txt"""