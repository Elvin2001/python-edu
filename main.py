words = ["Привет", "Круто", "Здесь", "Место", "Кот", "Рыбалка"]

for word in words:
    if "р" in word or "Р" in word:
        print(f"Слово '{word}' - картавое!")

num = 0
print("\n")

for i in range(0, 10):
    print(f"Current number: {num}")
    num += 1

my_number = 8

while True:
    for i in range(0, 10):
        i += 1
        if int(i) == my_number:
            print("Восьмёрка")
            break
        else:
            print("Восьмёрки не оказалось..")
