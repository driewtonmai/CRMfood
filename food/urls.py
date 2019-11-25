from django.urls import path

from food.views import *
app_name = 'food'


urlpatterns = [
    path('tables/', TablesCreateView.as_view(), name='tables'),
    path('tables/<int:pk>/', TablesRetrieveView.as_view()),
    path('roles/', RolesCreateView.as_view(), name='roles'),
    path('roles/<int:pk>', RolesRetrieveView.as_view()),
    path('departments/', DepartmentsCreateView.as_view(), name='departments'),
    path('departments/<int:pk>/', DepartmentsRetrieveView.as_view(), name='departments'),

]
