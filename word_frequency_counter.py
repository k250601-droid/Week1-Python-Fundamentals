text = input("Enter a paragraph: ").lower()
words = text.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequency:")
for word, count in freq.items():
    print(word, ":", count)