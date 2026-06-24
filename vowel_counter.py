text = input("Enter a sentence: ").lower()
vowels = "aeiou"

count = 0
for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)