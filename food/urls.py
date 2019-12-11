from django.urls import path
from food.views import *
from rest_framework.routers import DefaultRouter

app_name = 'food'

# router = DefaultRouter()
# router.register('mealsbydep', MealsByDepViewSet, base_name='departmentid')

urlpatterns = [
    path('tables/', TablesCreateView.as_view(), name='table_create'),
    path('tables/<int:pk>/', TablesRetrieveView.as_view(), name='table_retrieve'),

    path('roles/', RolesCreateView.as_view(), name='role_create'),
    path('roles/<int:pk>', RolesRetrieveView.as_view(), name='role_retrieve'),

    path('departments/', DepartmentsCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/', DepartmentsRetrieveView.as_view(), name='departments_retrieve'),

    path('users/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/', UserRetrieveView.as_view(), name='user_retrieve'),

    path('mealcategories/', MealCategoriesCreateView.as_view(), name='mealcategories_create'),
    path('mealcategories/<int:pk>/', MealCategoriesRetrieveView.as_view(), name='mealcategories_retrieve'),

    path('mealcategoriesbydepartment/<int:departmentid>/', MealsByDepView.as_view(),
         name='mealcategories_by_department'),

    path('mealsbycategory/<int:categoryid>/', MealsByCategoryView.as_view(), name='meals_by_category'),

    path('activeorders/', ActiveOrders.as_view(), name='active_orders'),

    path('meals/', MealsCreateView.as_view(), name='meals_create'),
    path('meals/<int:pk>/', MealsRetrieveView.as_view(), name='meals_retrieve'),

    path('statuses/', StatusesCreateView.as_view(), name='statuses_create'),
    path('statuses/<int:pk>/', StatusesRetrieveView.as_view(), name='statuses_retrieve'),

    path('service_percentage/', ServicePercentageCreateView.as_view(), name='service_percentage_create'),
    path('service_percentage/<int:pk>/', ServicePercentageRetrieveView.as_view(), name='service_percentage_retrieve'),

    path('orders', OrdersCreateView.as_view(), name='orders_create'),
    path('orders/<int:pk>/', OrdersRetrieveView.as_view(), name='orders_retrieve'),

    path('checks/', ChecksCreateView.as_view(), name='checks_create'),
    path('checks/<int:pk>', ChecksRetrieveView.as_view, name='checks_retrieve'),
]

# urlpatterns += router.urls
