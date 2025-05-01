from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email',)

    def create(self, validated_data):

        if len(validated_data['username']) < 6:
            raise serializers.ValidationError({"error": "Слишком короткий логин!"})

        if len(validated_data['password']) < 6:
            raise serializers.ValidationError({"error": "Слишком короткий пароль!"})

        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({"error": "Пользователь с таким email уже существует!"})

        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user