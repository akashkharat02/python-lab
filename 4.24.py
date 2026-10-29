import re

def split_sentences(text):
    
    abbreviations = [
        "Mr.", "Mrs.", "Ms.", "Dr.", "Prof.", "Sr.", "Jr.",
        "St.", "vs.", "etc.", "e.g.", "i.e."
    ]

    
    placeholders = {}
    for i, abbr in enumerate(abbreviations):
        placeholder = f"__ABBR{i}__"
        placeholders[placeholder] = abbr
        text = text.replace(abbr, placeholder)


    sentences = re.split(r'(?<=[.!?])\s+', text.strip())


    for i, abbr in enumerate(abbreviations):
        placeholder = f"__ABBR{i}__"
        sentences = [s.replace(placeholder, abbr) for s in sentences]

    return sentences


text = input("Enter a block of text:\n")


sentences = split_sentences(text)


print("\nSentences:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")