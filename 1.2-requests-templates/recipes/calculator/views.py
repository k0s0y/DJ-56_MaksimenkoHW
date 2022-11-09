from django.shortcuts import render
from django.http import Http404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipe_viewer(request):
    try:
        count = int(request.GET.get("servings", 1))
        recipe_name = request.path.strip("/")
        for recipe_nm, recipe_ingredient in DATA.items():
            if recipe_nm == recipe_name:
                if count < 0 or count == 1:
                    return render(request, 'calculator/index.html', context={'recipe': DATA[f'{recipe_nm}']})
                else:
                    ingredient_dict = {}
                    for ingredient, amount in recipe_ingredient.items():
                        ingredient_dict[ingredient] = round(amount * count, 2)
                    return render(request, 'calculator/index.html', context={'recipe': ingredient_dict})
    except Exception as e:
        raise Http404
