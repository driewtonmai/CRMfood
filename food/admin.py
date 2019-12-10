from django.contrib import admin

from food.models import *

admin.site.register(Tables)
admin.site.register(Roles)
admin.site.register(Departments)
admin.site.register(Users)
admin.site.register(Meals)
admin.site.register(MealCategories)
admin.site.register(Statuses)
admin.site.register(Orders)
admin.site.register(Checks)
admin.site.register(MealsCount)