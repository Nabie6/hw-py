words = ["apple", "banana", "cherry", "blueberry"]
longest = words[0]

for x in words:
    if len(x) > len(longest):
        longest = x

print("The longest word is", longest + ".")

sentence = "python is a great programming language"

words2 = sentence.split()

if len(words) < 2:
    print("Too short to modify")
else:
    for i in range(len(words2)):
        if i % 2 == 0:
            words2[i] = words2[i].capitalize()

    sentence = " ".join(words2)
    print(sentence)

num = input("Введите данные через пробел: ").split()
num1 = []

for i in num:
    if i not in num1:
        num1.append(i)

print(num1)
