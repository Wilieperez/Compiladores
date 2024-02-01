from collections import Counter
import re

file_path = r"c:\Users\wilie\Documents\Parcial 11\Compiladores\Programas\text_file.txt"

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = "".join(lines)
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")

words = re.findall(r'\b\w+\b', lines.lower())
linebreaks = re.findall(r'\n', lines.lower())

print("Words:",len(words))
print("Parragraphs:", len(linebreaks)+1)
print("Characters:", len(lines))