import string

stopwords = {
    "is", "am", "are", "was", "were",
    "the", "a", "an", "and", "or",
    "in", "on", "at", "to", "of",
    "for", "with", "this", "that",
    "it", "as", "by", "from",
    "be", "been", "being", "has", "have",
    "had", "do", "does", "did"
}


text = input("Enter a paragraph: ")

words = text.split()

cleaned_words = []

for word in words:
    
    clean_word = word.lower().strip(string.punctuation)

    if clean_word not in stopwords:
        cleaned_words.append(word)


cleaned_text = " ".join(cleaned_words)

print("\nOriginal Text:")
print(text)

print("\nCleaned Text:")
print(cleaned_text)