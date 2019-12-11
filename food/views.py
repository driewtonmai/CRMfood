from rest_framework import generics, viewsets
from .models import MealCategories
from food.serializers import *


# Tables views
class TablesCreateView(generics.ListCreateAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer


class TablesRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer


# Roles views
class RolesCreateView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class RolesRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


# Departments views
class DepartmentsCreateView(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class DepartmentsRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


# Users views
class UserCreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


# Meal Categories views
class MealCategoriesCreateView(generics.ListCreateAPIView):
    queryset = MealCategories.objects.all()
    serializer_class = MealCategoriesSerializer


class MealCategoriesRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealCategories.objects.all()
    serializer_class = MealCategoriesSerializer


# Meals views
class MealsCreateView(generics.ListCreateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


class MealsRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


# Statuses views
class StatusesCreateView(generics.ListCreateAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


class StatusesRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


# Service Percentage views
class ServicePercentageCreateView(generics.ListCreateAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer


class ServicePercentageRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer


# Orders views
class OrdersCreateView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrdersRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


# Checks views
class ChecksCreateView(generics.ListCreateAPIView):
    queryset = Checks.objects.all()
    serializer_class = ChecksSerializers


class ChecksRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checks.objects.all()
    serializer_class = ChecksSerializers


# Meals by departments view
class MealsByDepView(generics.ListAPIView):
    serializer_class = MealCategoriesSerializer

    def get_queryset(self):
        department = self.kwargs['departmentid']
        return MealCategories.objects.filter(departmentid=department)


# Meals by category view
class MealsByCategoryView(generics.ListAPIView):
    serializer_class = MealsSerializer

    def get_queryset(self):
        category = self.kwargs['categoryid']
        return Meals.objects.filter(categoryid=category)


# Active orders view
class ActiveOrders(generics.ListAPIView):
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return Orders.objects.filter(isitopen=True)