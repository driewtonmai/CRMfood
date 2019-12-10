from django.db import models
import datetime
from django.utils import timezone

STATUS = [
    ('to do', 'to do'),
    ('in progress', 'in progress'),
    ('done', 'done')
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

    def __str__(self):
        return self.name


class Users(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    surname = models.CharField(verbose_name='Surname', max_length=50)
    login = models.CharField(verbose_name='Login', max_length=50)
    password = models.CharField(verbose_name='Password', max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    roleid = models.ForeignKey('Roles', on_delete=models.CASCADE, verbose_name='RoleID')
    dateofadd = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return '{}, {}'.format(self.name, self.surname)

class GetUserToken(models.Model):
    roleid = models.ForeignKey('Roles', on_delete=models.CASCADE, verbose_name='RoleID')
    token = models.CharField(max_length=100)


class MealCategories(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    departmentid = models.ForeignKey('Departments', on_delete=models.CASCADE, verbose_name='DemartmentID')

    def __str__(self):
        return self.name


class Statuses(models.Model):
    name = models.CharField(choices=STATUS, max_length=30, verbose_name='Status')

    def __str__(self):
        return self.name


class ServicePercentage(models.Model):
    percentage = models.IntegerField(verbose_name="Percentage")


class Meals(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    categoryid = models.ForeignKey('MealCategories', on_delete=models.CASCADE, verbose_name='CategoryID')
    price = models.IntegerField(verbose_name='Price')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.name


class Orders(models.Model):
    waiterid = models.ForeignKey('Users', on_delete=models.CASCADE, verbose_name='Waiter')
    tableid = models.ForeignKey('Tables', on_delete=models.CASCADE, verbose_name='Table')
    isitopen = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def get_total_sum(self):
        return sum(meal.get_sum() for meal in self.mealsid.all())


class MealsCount(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='mealsid')
    name = models.ForeignKey(Meals, on_delete=models.CASCADE, verbose_name="Name")
    count = models.PositiveIntegerField(verbose_name='Count')

    def get_sum(self):
        return self.count * self.name.price


class Checks(models.Model):
    orderid = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Order')
    date = models.DateField(auto_now_add=True)
    servicefee = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE)
    mealsid = models.ForeignKey(MealsCount, on_delete=models.CASCADE, verbose_name='Meal')

    def get_totalsum(self):
        return self.orderid.get_total_sum() + self.servicefee.percentage

