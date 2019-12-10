from rest_framework import generics

from food.serializers import *


class TablesCreateView(generics.ListCreateAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer


class TablesRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer


class RolesCreateView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class RolesRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class DepartmentsCreateView(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class DepartmentsRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class UserCreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class MealCategoriesCreateView(generics.ListCreateAPIView):
    queryset = MealCategories.objects.all()
    serializer_class = MealCategoriesSerializer


class MealCategoriesRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealCategories.objects.all()
    serializer_class = MealCategoriesSerializer


class MealsCreateView(generics.ListCreateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


class MealsRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


class StatusesCreateView(generics.ListCreateAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


class StatusesRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


class ServicePercentageCreateView(generics.ListCreateAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer


class ServicePercentageRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer


class OrdersCreateView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrdersRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class ChecksCreateView(generics.ListCreateAPIView):
    queryset = Checks.objects.all()
    serializer_class = ChecksSerializers


class ChecksRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checks.objects.all()
    serializer_class = ChecksSerializers
