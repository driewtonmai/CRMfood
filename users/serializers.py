from rest_framework import serializers
from django.contrib.auth import authenticate

from users.models import User, Roles


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'name',)


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=3,
        write_only=True
    )

    token = serializers.CharField(
        max_length=255,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'login', 'email', 'roleid', 'dateofadd', 'phone', 'password', 'token')
        read_only_fields = ('dateofadd', 'token')

    def create(self, validated_data):
        return User.objects.create_user(
            **validated_data
        )


class LoginSerializer(serializers.Serializer):
    roleid = serializers.IntegerField(
        source='roles.id',
        read_only=True
    )
    login = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        login = data.get('login', None)
        password = data.get('password', None)

        if login is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(login=login, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'login': user.login,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    roleid = serializers.PrimaryKeyRelatedField(
        queryset=Roles.objects.all(),
        source='roles.id',
    )
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'login', 'email', 'roleid', 'dateofadd', 'phone', 'password', 'token')
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        role = validated_data.pop('roleid', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        if role is not None:
            instance.role = role['id']

        instance.save()

        return instance