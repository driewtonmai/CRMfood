from food.models import *
from rest_framework import serializers


class TablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ('name',)


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('name',)


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('name',)


class UsersSerializer(serializers.ModelSerializer):
    # roles = RolesSerializer(many=True)

    class Meta:
        model = Users
        fields = ('name', 'surname', 'login', 'password', 'email', 'dateofadd', 'phone', 'roleid',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        roles = validated_data.pop('roleid')

        users = Users.objects.create(**validated_data)

        for role in roles:
            Roles.objects.create(users=users, **role)

        return users


class MealCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategories
        fields = ('name', 'departmentid',)

    def create(self, validated_data):
        departments = validated_data.pop('departmentid')

        mealcategories = MealCategories.objects.create(**validated_data)

        for department in departments:
            Departments.objects.create(mealcategories=mealcategories, **department)

        return mealcategories