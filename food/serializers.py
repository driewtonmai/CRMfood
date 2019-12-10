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


class MealsCountSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    count = serializers.CharField(read_only=True)
    sum = serializers.IntegerField(read_only=True, source='get_sum')

    class Meta:
        model = MealsCount
        fields = ('id', 'name', 'count', 'sum')


class OrdersSerializer(serializers.ModelSerializer):
    mealsid = MealsCountSerializer(many=True)

    class Meta:
        model = Orders
        fields = ('id', 'waiterid', 'tableid', 'isitopen', 'date', 'mealsid',)


class ChecksSerializers(serializers.ModelSerializer):
    mealsid = MealsCountSerializer(read_only=True)
    servicefee = serializers.FloatField(read_only=True, source='servicefee.percentage')
    totalsum = serializers.FloatField(source='get_totalsum', read_only=True)

    class Meta:
        model = Checks
        fields = ('id', 'orderid', 'date', 'servicefee', 'totalsum', 'mealsid' )


