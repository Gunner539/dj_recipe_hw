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

def get_recipe(request):

    context = {
          'recipe': DATA.get(request.path.replace('/', '')),
          'servings': 1
        }
    try:
        servings_par = int(request.GET.get('servings', 1))
    except ValueError as ve:
        servings_par = 1
    #     print()
    if  servings_par != 1:
       for key, value in context['recipe'].items():
           context['recipe'][key] *= servings_par

       context['servings'] *= servings_par

    return render(request, 'calculator/index.html', context)

