from django.contrib import admin

from food.models import *


# class MealsCountInline(admin.StackedInline):
#     model = MealsCount
#     extra = 1
#
#
# class CheckAdmin(admin.ModelAdmin):
#     inlines = (MealsCountInline,)


admin.site.register(Tables)
admin.site.register(Departments)
admin.site.register(Meals)
admin.site.register(MealCategories)
admin.site.register(Statuses)
admin.site.register(Orders)
admin.site.register(Checks)
admin.site.register(MealsCount)
admin.site.register(ServicePercentage)