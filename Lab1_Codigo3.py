from collections import Counter
import re

file_path = r"c:\Users\wilie\Documents\Parcial 11\Compiladores\Programas\text_file.txt"

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        nocomment_lines = [line.split('//')[0].rstrip() for line in lines]
        nocomment_lines = " ".join(nocomment_lines)
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")

raw_lines = nocomment_lines.replace('.', '').replace(',', '')
words = re.findall(r'\b\w+\b', raw_lines.lower())
word_counts = Counter(words)

for word, count in word_counts.items():
    print(f"{word}: {count}")