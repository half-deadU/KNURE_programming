import hashlib

def generate_file_hashes(*file_paths):
    hashes = {}
    for path in file_paths:
        try:
            with open(path, 'rb') as f:
                file_content = f.read()
                sha256_hash = hashlib.sha256(file_content).hexdigest()
                hashes[path] = sha256_hash
        except FileNotFoundError:
            print(f"Помилка: файл '{path}' не знайдено.")
        except IOError:
            print(f"Помилка: не вдалося прочитати файл '{path}'.")
    return hashes

if __name__ == "__main__":
    print("Введіть шляхи до файлів через кому:")
    input_paths = input().strip()
    paths = [p.strip() for p in input_paths.split(',') if p.strip()]

    results = generate_file_hashes(*paths)

    if results:
        print("\nХеші файлів (SHA-256):")
        for file_path, file_hash in results.items():
            print(f"{file_path}: {file_hash}")
