with open('recipes.txt', 'r', encoding='utf-8') as recipes:  # читаем файл
    recipes = recipes.read()
    cook_book = {}
    splitted_recipes = recipes.split('\n\n')  # разбиваем по двум переходам на новую строку
    for recipe in splitted_recipes:  # цикл по каждому рецепту
        item = recipe.split('\n')  # отдельный рецепт
        dish, ingredient_count, ingredients = item[0], item[1], item[2:]  # разбитие на блюдо, ингредиенты
        ingredient_list = []
        for ingredient in ingredients:  # цикл по ингредиентам
            name, quantity, measure = ingredient.split('|')  # разбиваем по '|'
            ingredient_list.append({  # добавляем в список словари с каждым ингредиентом
                'ingredient_name': name,
                'quantity': int(quantity),
                'measure': f'{measure}.'
            })
        cook_book[dish] = ingredient_list  # добавляем словарь Ключ-название блюда : Значение-список с ингредиентами


def get_shop_list_by_dishes(dishes, person_count):  # создаем функцию
    if not isinstance(dishes, list):  # проверяем, что в dishes нам передают список
        return 'Not list'
    ingredient_dict = {}
    for dish in dishes:  # идем циклом по списку блюд
        if dish not in cook_book:  # проверяем есть ли блюдо в книге
            print(f'Блюда - {dish} нет в книге!')
        else:
            ingredients = cook_book[dish]  # достаем ингредиенты
            for ingredient in ingredients:  # идем циклом по ингредиентам
                if ingredient['ingredient_name'] in ingredient_dict:  # проверяем наличие ингредиента в словаре
                    ingredient_dict[ingredient['ingredient_name']]['quantity'] += ingredient[
                                                                                      'quantity'] \
                                                                                  * person_count  # сложение количества
                else:
                    info_dict = {  # создаем словарь с мерами и количеством с учетом количества людей
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                    ingredient_dict[ingredient['ingredient_name']] = info_dict  # добавляем в словарь
    if not ingredient_dict:  # проверяем не пустой ли словарь
        return ''  # если пустой возвращаем пустую строку
    else:
        return ingredient_dict  # если не пустой возвращаем словарь в ингредиентами


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
