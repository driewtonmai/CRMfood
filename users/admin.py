from django.contrib import admin
from users.models import User, Roles


admin.site.register(User)
admin.site.register(Roles)
