from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView,
    DishDetailView,
    CookDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView
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
    path(
        "dishtype/update/<int:pk>/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dishtype/delete/<int:pk>/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),

    path("dish/",
         DishListView.as_view(),
         name="dish-list"),
    path(
        "dish/create/",
        DishCreateView.as_view(),
        name="dish-create",
    ),
    path(
        "dish/update/<int:pk>/",
        DishUpdateView.as_view(),
        name="dish-update",
    ),
    path(
        "dish/delete/<int:pk>/",
        DishDeleteView.as_view(),
        name="dish-delete",
    ),
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
