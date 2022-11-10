from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from kitchen.models import Cook, Dish, DishType


@login_required
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


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dishes_type_list"
    template_name = "kitchen/dishes_type_list.html"
    paginate_by = 5


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.select_related("dish_type")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 1


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class CookDetailView (LoginRequiredMixin, generic.DetailView):
    model = Cook
    context_object_name = "cooks"
    queryset = Cook.objects.prefetch_related("dishes__dish_type")
