from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
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


def index(request):
    context = {'dishes': DATA.keys()}
    return render(request, 'calculator/index.html', context)


def calculator_view(request, ingredient):
    serving = int(request.GET.get('serving', '1'))
    context = {
        'dish': ingredient,
        'recipe': {key: value * serving for key, value in DATA.get(ingredient).items()},
        'serving': serving,
    }
    return render(request, 'calculator/calculator.html', context)
