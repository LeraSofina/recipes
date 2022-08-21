with open('ingredients.txt', 'r', encoding='UTF-8') as file:

    cook_book = {}
    for line in file:
        recipe = []
        dish = line.strip()
        ingredient_quantity = file.readline().strip()
        for ingredient in range(int(ingredient_quantity)):
            ingredient = file.readline().strip().split('|')
            recipe.append({'ingredient_name': ingredient[0],
                           'quantity': int(ingredient[1]),
                           'measure': ingredient[2]})
        empty_string = file.readline()
        cook_book[dish] = recipe
    from pprint import pprint
    pprint(cook_book)


    def get_shop_list_by_dishes(dishes, person_count):
        for dish in dishes:
            for key, value in cook_book.items():
                if dish in key:
                    for val in value:
                        amount = val['quantity'] * int(person_count)
                        print({val['ingredient_name']: {'measure': val['measure'], 'quantity': amount}})

    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)






