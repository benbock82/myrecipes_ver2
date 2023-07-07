from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.CustomSignUpView.as_view(), name='signup'),
    path('reset_password/', views.CustomPasswordResetView.as_view(), name='reset_password'),
    path('reset_password/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password/complete/', views.CustomPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('account/', views.AccountView.as_view(), name='account'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.AccountView.as_view()),
    path('upload_recipe/', views.RecipeCreateView.as_view(), name='upload_recipe'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('browse_recipes', views.BrowseRecipes.as_view(), name='browse_recipes'),
    path('search_recipes', views.SearchRecipeView.as_view(), name='search_recipes'),
    path('edit_recipe/<int:pk>/', views.EditRecipeView.as_view(), name='edit_recipe'),
    path('delete_recipe/<int:pk>/', views.DeleteRecipeView.as_view(), name='delete_recipe'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('change_password', views.ChangePasswordView.as_view(), name='change_password'),
    path('contact_us/', views.ContactUsView.as_view(), name='contact_us'),
    path('contact_us/success/', views.ContactUsSuccessView.as_view(), name='contact_us_success'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('admin_tools/', views.AdminToolsView.as_view(), name='admin_tools'),
    path('faq/', views.FaqView.as_view(), name='faq'),
]