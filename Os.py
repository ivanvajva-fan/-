import shutil
import os

source_folder = "h"
backup_folder = "hh"

# Создаём папку для резервных копий, если её нет
os.makedirs(backup_folder, exist_ok=True)

# Копируем файлы и удаляем оригиналы
for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)
    backup_path = os.path.join(backup_folder, filename)
    
    # Проверяем, что это файл, а не папка
    if os.path.isfile(source_path):
        try:
            shutil.copy(source_path, backup_path)
            
            # Добавляем проверку существования скопированного файла
            if os.path.exists(backup_path):
                os.remove(source_path)  # Удаляем, только если копирование прошло успешно
            else:
                print(f"Ошибка: Файл {filename} не был успешно скопирован.")
                
        except Exception as e:
            print(f"Ошибка при копировании {filename}: {e}")
