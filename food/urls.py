from django.urls import path
from food.views import *
app_name = 'food'

urlpatterns = [
    path('tables/', TablesCreateView.as_view(), name='table_create'),
    path('tables/<int:pk>/', TablesRetrieveView.as_view(), name='table_retrieve'),
    path('roles/', RolesCreateView.as_view(), name='role_create'),
    path('roles/<int:pk>', RolesRetrieveView.as_view(), name='role_retrieve'),
    path('departments/', DepartmentsCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/', DepartmentsRetrieveView.as_view(), name='departments_retrieve'),
    path('users/', UserCreateView.as_view(), name='user_create'),
    path('mealcategories/', MealCategoriesCreateView.as_view(), name='mealcategories_create'),
    path('mealcategories/<int:pk>/', MealCategoriesRetrieveView.as_view(), name='mealcategories_retrieve')
]
