text = input("Enter the text: ")
query = input("Enter the search term: ")


lower_text = text.lower()
lower_query = query.lower()


count = lower_text.count(lower_query)


highlighted_text = ""
i = 0

while i < len(text):
    if lower_text.startswith(lower_query, i):
        highlighted_text += "**" + text[i:i + len(query)] + "**"
        i += len(query)
    else:
        highlighted_text += text[i]
        i += 1

print("\nNumber of occurrences:", count)
print("Highlighted text:")
print(highlighted_text)

