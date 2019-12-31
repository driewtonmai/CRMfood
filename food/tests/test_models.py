from django.test import TestCase
from food.models import *
from users.models import *


class ModelTests(TestCase):

    def create_tables(self, name='1'):
        return Tables.objects.create(name=name)

    def test_tables_creation(self):
        tables = self.create_tables()
        self.assertTrue(isinstance(tables, Tables))
        self.assertEqual(tables.__str__(), tables.name)


    def create_departments(self, name="Kitchen"):
        return Departments.objects.create(name=name)

    def test_departments_creation(self):
        departments = self.create_departments()
        self.assertTrue(isinstance(departments, Departments))
        self.assertEqual(departments.__str__(), departments.name)


    def create_meal_categories(self, name="salad"):
        department = self.create_departments()
        return MealCategories.objects.create(name=name, departmentid=department)

    def test_meal_categories_creation(self):
        meal_categories = self.create_meal_categories()
        self.assertTrue(isinstance(meal_categories, MealCategories))
        self.assertEqual(meal_categories.__str__(), meal_categories.name)


    def create_statuses(self, name='to do'):
        return Statuses.objects.create(name=name)

    def test_statuses_creation(self):
        statuses = self.create_statuses()
        self.assertTrue(isinstance(statuses, Statuses))
        self.assertEqual(statuses.__str__(), statuses.name)


    def create_service_percentage(self, percentage=32):
        return ServicePercentage.objects.create(percentage=percentage)

    def test_service_percentage_creation(self):
        service_percentage = self.create_service_percentage()
        self.assertTrue(isinstance(service_percentage, ServicePercentage))
        self.assertEqual(service_percentage.__str__(), service_percentage.percentage)


    def create_meals(self, name="Ceaser", price=190, description='very tasty salad with cheezzz'):
        meals_categories = self.create_meals()
        return Meals.objects.create(name=name, categoryid=meals_categories, price=price, description=description)

    def test_meals_creation(self):
        meals = Meals.objects.create()
        self.assertTrue(isinstance(meals, Meals))
        self.assertEqual(meals.__str__(), meals.name)


    def create_roles(self, name="waiter"):
        return Roles.objects.create(name=name)

    def test_roles_creation(self):
        roles = Roles.objects.create()
        self.assertTrue(isinstance(roles, Roles))
        self.assertEqual(roles.__str__(), roles.name)


    # def create_user(self, login, password):



    def create_orders(self, isitopen=True):
        tableid = self.create_tables()
        waiterid = ...
        return Orders.objects.create(waiterid=waiterid, isitopen=isitopen, tableid=tableid)

    def test_orders_creation(self):
        orders = Orders.objects.create()
        self.assertTrue(isinstance(orders, Orders))
        self.assertEqual(orders.__str__(), '{}, {}'.format(orders.waiterid, orders.tableid))
