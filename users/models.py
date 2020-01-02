import jwt

from datetime import datetime, timedelta
from django.db import models

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser)


class UserManager(BaseUserManager):
    def create_user(self, login, email, password=None, name=None, surname=None, roleid=None, phone=None):
        if not login:
            raise ValueError('The given login must be set')

        user = self.model(
            name=name,
            surname=surname,
            login=login,
            email=email,
            roleid=roleid,
            phone=phone
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, login, email, password):
        if not login:
            raise ValueError('The given login must be set')
        if not password:
            raise ValueError('The given password must be set')

        user = self.create_user(login, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(verbose_name='Name', max_length=222, null=True)
    surname = models.CharField(verbose_name='Surname', max_length=222, null=True)
    login = models.CharField(verbose_name='Login', max_length=222, unique=True)
    password = models.CharField(verbose_name='Password', max_length=222)
    email = models.EmailField(max_length=50, unique=True, db_index=True)
    roleid = models.ForeignKey('Roles', null=True, on_delete=models.SET_NULL, verbose_name='RoleID')
    phone = models.CharField(verbose_name='Phone', max_length=222, null=True)
    dateofadd = models.DateField(auto_now_add=True)
    date_of_update = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.login

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return '{} {}'.format(self.name, self.surname)

    def get_short_name(self):
        return self.name

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class Roles(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)

    def __str__(self):
        return self.name


class GetUserToken(models.Model):
    roleid = models.ForeignKey('Roles', on_delete=models.CASCADE, verbose_name='RoleID')
    token = models.CharField(max_length=100)
