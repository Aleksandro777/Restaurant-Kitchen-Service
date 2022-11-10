from django.shortcuts import render
from django.views import generic

from kitchen.models import Cook, Dish, DishType


def index(request):
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dishes_type_list"
    template_name = "kitchen/dishes_type_list.html"
    paginate_by = 5


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.select_related("dish_type")


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish


class CookDetailView (generic.DetailView):
    model = Cook
    context_object_name = "cooks"
    queryset = Cook.objects.prefetch_related("dishes__dish_type")
