from django.contrib import admin

from food.models import *

admin.site.register(Tables)
admin.site.register(Roles)
admin.site.register(Departments)
admin.site.register(Users)
admin.site.register(Meals)
admin.site.register(MealCategories)