shopping_list = ["Яблоки", "Молоко"]
destination = input("Куда пойдёте, Сударь?\n")

if destination.lower() == "пикник":
    print("Надо не забыть купить мясо и дрова!")
    shopping_list.extend(["Мясо", "Дрова"])

elif destination.lower() == "гости":
    print("Надо не забыть купить торт и вино!")
    shopping_list.extend(["Торт", "Вино"])

else:
    print("Хорошо, что никуда сегодня не идём... нужно что-то вкусненькое купить!")
    shopping_list.extend(["Мороженое", "Попкорн"])

print(f"Всего товаров в корзине - {len(shopping_list)}\n, ваш список товаров: [{shopping_list}].")
