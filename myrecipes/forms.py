from django import forms
from .models import Recipe
from multiupload.fields import MultiFileField
from django.contrib.auth.forms import UserCreationForm


class RecipeForm(forms.ModelForm):
    images = MultiFileField(min_num=1, max_num=1, max_file_size=1024*1024, required=False)

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cuisines_text', 'ingredients_text', 'cooking_method_text',
                  'images', 'youtube_url']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'description': 'Description',
            'youtube_url': 'Youtube URL',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].required = False


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

