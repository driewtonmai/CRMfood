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

# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields =
