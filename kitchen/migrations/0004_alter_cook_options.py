# Generated by Django 4.1.3 on 2022-11-10 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0003_alter_dish_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cook",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
    ]
