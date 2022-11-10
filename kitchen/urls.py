from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView,
    DishDetailView,
    CookDetailView,
    DishTypeCreateView
)

urlpatterns = [
    path("", index, name="index"),
    path("dishtype/",
         DishTypeListView.as_view(),
         name="dish-type-list"),
    path(
        "dishtype/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),

    path("dish/",
         DishListView.as_view(),
         name="dish-list"),
    path("cook/",
         CookListView.as_view(),
         name="cook-list"),
    path("dish/<int:pk>/",
         DishDetailView.as_view(),
         name="dish-detail"),
    path("cook/<int:pk>/",
         CookDetailView.as_view(),
         name="cook-detail"),
]

app_name = "kitchen"
