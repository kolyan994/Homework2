from pprint import pprint
with open('Cook_book.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        count_of_ingr = int(f.readline())
        ingredients = []
        for _ in range(count_of_ingr):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            ingredient = {
                'ingredient_name': ingredient_name,
                'measure': measure,
                'quantity': quantity

            }
            ingredients.append(ingredient)
        f.readline()
        cook_book[dish_name] = ingredients
    pprint(cook_book)



def get_shop_list_by_dishes(dishes, person_count : int):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for i in cook_book[dish]:
                if i['ingredient_name'] not in result:
                    result[i['ingredient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
                else:
                    result[i['ingredient_name']]['quantity'] += int(i['quantity']) * person_count

    return result

pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Фахитос'], 4))


def zadacha3():
    dct = {}
    f1 = open('file1.txt', encoding='utf-8')
    linecount1 = len(f1.readlines())
    dct['file1.txt'] = linecount1
    f1.close()
    f2 = open('file2.txt', encoding='utf-8')
    linecount2 = len(f2.readlines())
    dct['file2.txt'] = linecount2
    f2.close()
    f3 = open('file3.txt', encoding='utf-8')
    linecount3 = len(f3.readlines())
    dct['file3.txt'] = linecount3
    f3.close()
    sdct = sorted(dct, key=dct.get)
    for f in sdct:
        f2 = open('file4.txt', 'a', encoding='utf-8')
        f1 = open(f, encoding='utf-8')
        f2.write(f + '\n')
        f2.write(str(dct[f]) + '\n')
        w = f1.readlines()
        w.append('\n')
        f2.writelines(w)

    f1.close()
    f2.close()
    f3.close()

zadacha3()