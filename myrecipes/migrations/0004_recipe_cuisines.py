# Generated by Django 4.2.2 on 2023-06-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrecipes', '0003_remove_recipe_cuisines_remove_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cuisines',
            field=models.ManyToManyField(blank=True, to='myrecipes.cuisinetag'),
        ),
    ]