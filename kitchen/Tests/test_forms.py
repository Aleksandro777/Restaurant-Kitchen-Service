from django.test import TestCase

from kitchen.form import CookCreateForm, CookYearExperienceUpdateForm


class FormsTests(TestCase):
    def test_cook_creation_form(self):
        form_data = {
            "username": "test_user",
            "password1": "user1234",
            "password2": "user1234",
            "years_of_experience": 10,
            "first_name": "test_name",
            "last_name": "test_last_name",
        }

        form = CookCreateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_cook_update_form(self):
        form_data = {"years_of_experience": 10}

        form = CookYearExperienceUpdateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
