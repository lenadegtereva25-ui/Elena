import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task(file) -> None:
    with open(file, "r") as f:
        content = csv.DictReader(f)
        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as new_file:
            json_data= [row for row in content]
            json.dump(json_data, new_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

