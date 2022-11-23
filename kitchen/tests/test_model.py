from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="test_name",
        )
        self.assertEqual(str(dish_type), f"{dish_type.name}")

    def test_cook_str(self):
        username = "test_username"
        first_name = "test_first_name"
        last_name = "test_last_name"
        cook = get_user_model().objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        self.assertEqual(str(cook), f"{username} ({first_name} {last_name})")

    def test_dish_str(self):
        name = "test_name"
        description = "test_description"
        price = 10

        dish_type = DishType.objects.create(
            name=name,
        )
        dish = Dish.objects.create(
            name=name,
            description=description,
            price=price,
            dish_type=dish_type,
        )

        self.assertEqual(str(dish), name)

    def test_create_cook_with_years_of_experience(self):
        username = "test_username"
        password = "test_pass"
        first_name = "test_first_name"
        last_name = "test_last_name"
        years_of_experience = 100
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            years_of_experience=years_of_experience,
        )

        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.first_name, first_name)
        self.assertEqual(cook.last_name, last_name)
        self.assertEqual(cook.years_of_experience, years_of_experience)
