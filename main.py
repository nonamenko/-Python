def word_counter(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            print(f"Кількість слів у файлі: {len(words)}")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Сталася помилка:", e)

if __name__ == "__main__":
    file_path = input("Введіть шлях до текстового файлу: ")
    word_counter(file_path)
