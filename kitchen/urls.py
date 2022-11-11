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
    DishDeleteView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    delete_cook_from_dish,
    assign_cook_to_dish,
)

urlpatterns = [
    path("", index, name="index"),
    path("dishtype/", DishTypeListView.as_view(), name="dish-type-list"),
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
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
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
    path("cook/", CookListView.as_view(), name="cook-list"),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path(
        "cook/create/",
        CookCreateView.as_view(),
        name="cook-create",
    ),
    path(
        "cook/update/<int:pk>/",
        CookUpdateView.as_view(),
        name="cook-update",
    ),
    path("cook/delete/<int:pk>/", CookDeleteView.as_view(), name="cook-delete"),
    path(
        "cook/<int:pk>/assign_to_dish/",
        assign_cook_to_dish,
        name="cook-assign-to-dish",
    ),
    path(
        "cook/<int:pk>/delete_from_dish/",
        delete_cook_from_dish,
        name="cook-delete-from-dish",
    ),
]

app_name = "kitchen"
