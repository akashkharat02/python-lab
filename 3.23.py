import re
input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

target = input("Enter target word/phrase: ")
replacement = input("Enter replacement word/phrase: ")

choice = input("Case-insensitive replacement? (yes/no): ")

with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()


if choice.lower() == "yes":

    modified_text = re.sub(re.escape(target), replacement, text, flags=re.IGNORECASE)
else:

    modified_text = text.replace(target, replacement)

with open(output_file, "w", encoding="utf-8") as file:
    file.write(modified_text)

print("\nFind-and-replace operation completed successfully.")
print("Modified file saved as:", output_file)