word = input("write ")
sword = len(word)
ini = "a"
print(word)
print(sword)

for letter in word:
    if letter in word == ini:
        print("ini")
    else:
        continue
