import os
import shutil
import argparse

def copy_and_sort_files(src_dir, dst_dir='dist'):
    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            if os.path.isdir(item_path):
                copy_and_sort_files(item_path, dst_dir)
            elif os.path.isfile(item_path):
                file_ext = os.path.splitext(item)[1][1:].lower()
                
                target_dir = os.path.join(dst_dir, file_ext)
                os.makedirs(target_dir, exist_ok=True)
                target_path = os.path.join(target_dir, item)
                shutil.copy2(item_path, target_path)
                print(f"Скопійовано: {item_path} до {target_path}")
    except Exception as e:
        print(f"Помилка {e}")

def main():
    parser = argparse.ArgumentParser(description="Рекурсивне сортування файлів.")
    parser.add_argument("source")
    parser.add_argument("destination", default="output")
    args = parser.parse_args()

    src_dir = args.source
    dst_dir = args.destination

    if not os.path.exists(src_dir):
        print("Вихідна директорія не існує.")
        return

    print(f"Копіювання з '{src_dir}' у '{dst_dir}'...")
    copy_and_sort_files(src_dir, dst_dir)
    print("Готово")

if __name__ == "__main__":
    main()
