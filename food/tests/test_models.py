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

    def create_meals(self, name="Ceaser", price=190, description='very tasty salad with cheezzz'):
        meals_categories = self.create_meal_categories()
        return Meals.objects.create(name=name, price=price, description=description, categoryid=meals_categories)

    def test_meals_creation(self):
        meals = self.create_meals()
        self.assertTrue(isinstance(meals, Meals))
        self.assertEqual(meals.__str__(), meals.name)

    def create_roles(self, name="waiter"):
        return Roles.objects.create(name=name)

    def test_roles_creation(self):
        roles = self.create_roles()
        self.assertTrue(isinstance(roles, Roles))
        self.assertEqual(roles.__str__(), roles.name)

    def create_user(self, login, email, password, name, surname, phone, roleid):
        roles = self.create_roles()
        return User.objects.create_user(login=login, email=email, password=password, name=name,
                                        surname=surname, phone=phone, roleid=roles)

    def test_user_creation(self):
        roles = self.create_roles()
        user = self.create_user(login='user', email='user@bk.ru', password='1234', name='Abdulla',
                                surname='Mahadjimov', phone='1213243', roleid=roles)
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), user.login)


    def create_superuser(self, login, email, password):
        return User.objects.create_superuser(login=login, email=email, password=password)

    def test_superuser_creation(self):
        user = self.create_superuser(login='admin', email='admin@bk.ru', password='1234')
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), user.login)


    def create_orders(self, isitopen=True):
        roles = self.create_roles()
        tableid = self.create_tables()
        waiterid = self.create_user(login='uuser', email='useer@bk.ru', password='1234', name='Abdulla',
                                surname='Mahadjimov', phone='1213243', roleid=roles)
        return Orders.objects.create(waiterid=waiterid, isitopen=isitopen, tableid=tableid)

    def test_orders_creation(self):
        orders = self.create_orders()
        self.assertTrue(isinstance(orders, Orders))
        self.assertEqual(orders.__str__(), '{}, {}'.format(orders.waiterid, orders.tableid))


    def create_meals_count(self, count=2):
        order = self.create_orders()
        name = self.create_meals()
        return MealsCount.objects.create(name=name, order=order, count=count)

    def test_meals_count_creation(self):
        meals_count = self.create_meals_count()
        self.assertTrue(isinstance(meals_count, MealsCount))


    # def create_checks(self):
    #     orderid = self.create_orders()
    #     servicefee = self.create_service_percentage()
    #     mealsid = self.create_meals_count()
    #     return Checks.objects.create(orderid=orderid, servicefee=servicefee, mealsid=mealsid)
    #
    # def test_checks_creation(self):
    #     checks = self.create_checks()
    #     self.assertTrue(isinstance(checks, Checks))