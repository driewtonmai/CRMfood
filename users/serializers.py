from rest_framework import serializers
from users.models import User, Roles

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'login', 'email', 'roleid', 'dateofadd', 'phone', )
        extra_kwargs = {'password': {'write_only': True}}


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'name',)