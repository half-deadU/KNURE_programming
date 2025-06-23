import hashlib

def generate_file_hashes(*input_paths):
    results = {}
    for input_path in input_paths:
        try:
            with open(input_path, 'rb') as f:
                file_content = f.read()
                sha256_hash = hashlib.sha256(file_content).hexdigest()
                results[input_path] = sha256_hash
        except FileNotFoundError:
            print(f"Помилка: файл '{input_path}' не знайдено.")
        except IOError:
            print(f"Помилка: не вдалося прочитати файл '{input_path}'.")
    return results

if __name__ == "__main__":
    print("Введіть шляхи до файлів через кому:")
    input_paths = [p.strip() for p in input().strip().split(',') if p.strip()]

    results = generate_file_hashes(*input_paths)

    if results:
        print("\nХеші файлів (SHA-256):")
        for input_path, file_hash in results.items():
            print(f"{input_path}: {file_hash}")

""""""