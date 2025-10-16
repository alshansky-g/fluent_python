import os
import time
from rich.console import Console
print = Console().print

query = input("Что ищем?\n>>")
timestamp = int(input("Сколько часов назад примерно был создан файл?\n>>") or 0) or 48

path = "/home"
matches = []

for address, dirs, files in os.walk(path):
    for file in files:
        if query.lower() in file.lower():
            full_path = os.path.join(address, file)

            if timestamp:
                if time.time() - os.path.getctime(full_path) < timestamp*3600:
                    matches.append(full_path)
            else:
                matches.append(full_path)

print("\n[green]Найденные результаты:")
for i, result in enumerate(matches, 1):
    print(f"[green]{i}. [blue]{result}")