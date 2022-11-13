from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Dish, Cook

TYPE_DISH_LIST_URL = reverse("kitchen:dish-type-list")
COOK_LIST_URL = reverse("kitchen:cook-list")
DISH_LIST_URL = reverse("kitchen:dish-list")
HOME_PAGE_URL = reverse("kitchen:index")


class PublicTests(TestCase):
    def test_dish_list_login_required(self):
        response = self.client.get(DISH_LIST_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_type_dish_list_login_required(self):
        response = self.client.get(TYPE_DISH_LIST_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_cook_login_required(self):
        response = self.client.get(COOK_LIST_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_index_login_required(self):
        response = self.client.get(HOME_PAGE_URL)

        self.assertNotEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(reverse("login"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")


class PrivateTests(TestCase):
    def setUp(self) -> None:
        DishType.objects.create(name="test")
        DishType.objects.create(name="test1")
        Dish.objects.create(
            name="test_name", description="Hello World", price=2.22, dish_type_id=1
        )
        Dish.objects.create(
            name="test_name1", description="Hello World1", price=3.22, dish_type_id=2
        )
        self.user = get_user_model().objects.create_user(
            username="test_username", password="test1234"
        )
        self.client.force_login(self.user)

    def test_dish_type_list(self):
        response = self.client.get(TYPE_DISH_LIST_URL)
        dish_type = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dishes_type_list"]),
            list(dish_type),
        )
        self.assertTemplateUsed(response, "kitchen/dishes_type_list.html")

    def test_dish_list(self):
        response = self.client.get(DISH_LIST_URL)
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes),
        )
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_dish_detail(self):
        response = self.client.get(reverse("kitchen:dish-detail", args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_detail.html")

    def test_cook_list(self):
        response = self.client.get(COOK_LIST_URL)
        cooks = Cook.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks),
        )
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_cook_detail(self):
        response = self.client.get(reverse("kitchen:cook-detail", args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cook_detail.html")

    def test_create_cook(self):
        form_data = {
            "username": "test_user",
            "password1": "test_pass123",
            "password2": "test_pass123",
            "first_name": "Test first_name",
            "last_name": "Test last_name",
            "years_of_experience": 10,
        }

        self.client.post(reverse("kitchen:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])
