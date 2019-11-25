from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

STATUS = [
    (1, 'to-do'),
    (2, 'in progress'),
    (3, 'done')
]

TABLES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]


class Tables(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)

    def __str__(self):
        return self.name


class Roles(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)

    def __str__(self):
        return self.name


class Departments(models.Model):
        name = models.CharField(verbose_name='Name', max_length=50)


class Users(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    surname = models.CharField(verbose_name='Name', max_length=50)
    login = models.CharField(verbose_name='Name', max_length=50)
    password = models.CharField(verbose_name='Password', max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    roleid = models.ForeignKey('Roles', on_delete=models.CASCADE, verbose_name='RoleID', related_name='Users')
    dateoffadd = models.DateField()
    phone = models.CharField(max_length=50)


class GetUserToken(models.Model):
    roleid = models.ForeignKey('Roles', on_delete=models.CASCADE, verbose_name='RoleID', related_name='GetUserToken')
    token = models.CharField(max_length=100)


class MealCategories(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    departmentid = models.ForeignKey('Departments', on_delete=models.CASCADE, verbose_name='DemartmentID', related_name='MealCategories')


# class MealCategoriesByDepartment(models.Model):
#     name = models.CharField(verbose_name='Name', max_length=50)
#     departmentid = models.ForeignKey('Departments', on_delete=models.CASCADE, verbose_name='DemartmentID', related_name='MealCategories')


class Statuses(models.Model):
    name = models.IntegerField(choices=STATUS, verbose_name='Status')


class ServicePercentage(models.Model):
    percentage = models.IntegerField(verbose_name="Percentage")


class Meals(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    categoryid = models.ForeignKey('MealCategories', on_delete=models.CASCADE, related_name='Meals', verbose_name='CategoryID')
    price = models.IntegerField(verbose_name='Price')
    description = models.TextField(verbose_name='Description')


class Orders(models.Model):
    waiterid = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='Orders', verbose_name='Waiter')
    tableid = models.ForeignKey('Tables', on_delete=models.CASCADE, related_name='Orders', verbose_name='Table')
    tablename = models.IntegerField(choices=TABLES, verbose_name='Number of table')
    isitopen = models.BooleanField()
    date = models.DateField()
    mealsid = models.ForeignKey('Meals', on_delete=models.CASCADE, related_name='Orders', verbose_name='Meal')


class Checks(models.Model):
    orderid = models.ForeignKey('Orders', on_delete=models.CASCADE, related_name='Checks', verbose_name='Order')
    date = models.DateField()
    servicefee = models.ForeignKey('ServicePercentage', on_delete=models.CASCADE, related_name='Checks',)
    totalsum = models.IntegerField()
    meals = models.ForeignKey('Meals', on_delete=models.CASCADE, related_name='Checks')


# class Password(models.Model):
#     userid = ...
#     oldpassword =
#     newpassword =