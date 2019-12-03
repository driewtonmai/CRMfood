from food.models import *
from rest_framework import serializers


class TablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ('id', 'name',)


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'name',)


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('id', 'name',)


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'surname', 'login', 'password', 'email', 'dateofadd', 'phone', 'roleid',)
        extra_kwargs = {'password': {'write_only': True}}


class MealCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategories
        fields = ('id', 'name', 'departmentid',)


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ('id', 'name', 'categoryid', 'price', 'description',)


class StatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = ('id', 'name',)

class ServicePercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = ('percentage',)