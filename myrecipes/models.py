from django.db import models
from django.contrib.auth.models import User
from .utilities import extract_matching_ingredients
from storages.backends.s3boto3 import S3StaticStorage


class CuisineTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'myrecipes'


class IngredientTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'myrecipes'


class Recipe(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients_text = models.TextField()
    cooking_method_text = models.TextField()
    cuisines_text = models.CharField(max_length=1000, blank=True)
    cuisines_tag = models.ManyToManyField(CuisineTag)
    ingredient_tag = models.ManyToManyField(IngredientTag)
    image = models.ImageField(upload_to='recipe/', storage=S3StaticStorage, blank=True, null=True)  # Updated field
    youtube_url = models.URLField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_recipes')

    def __str__(self):
        return self.title

    def get_likes_count(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        # Check if the image field is being cleared
        if self.image is None and self.pk:
            # Delete the old image from storage
            old_image = Recipe.objects.get(pk=self.pk).image
            old_image.delete(save=False)

        super().save(*args, **kwargs)

        # Extract cuisines from cuisines_text and save as individual tags
        cuisines_list = [tag.strip("#").lower() for tag in self.cuisines_text.split("#") if tag.strip()]
        self.cuisines_tag.clear()
        for cuisine_name in cuisines_list:
            cuisine_tag, _ = CuisineTag.objects.get_or_create(name=cuisine_name)
            self.cuisines_tag.add(cuisine_tag)

        # Extract ingredient tags from ingredients_text and save as individual tags
        ingredient_tags = extract_matching_ingredients(self.ingredients_text)
        self.ingredient_tag.clear()
        for ingredient_tag in ingredient_tags:
            ingredient, _ = IngredientTag.objects.get_or_create(name=ingredient_tag)
            self.ingredient_tag.add(ingredient)

    class Meta:
        app_label = 'myrecipes'


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    comment_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        app_label = 'myrecipes'

