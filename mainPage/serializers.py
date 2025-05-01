from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth.models import User

from .models import Attacks

class AttacksSerializer(serializers.ModelSerializer):

    Author = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all())
    Author = serializers.HiddenField(
        default = CurrentUserDefault(),
    )

    class Meta:
        model = Attacks
        fields = '__all__'

class UpdateAttack(serializers.ModelSerializer):

    Author = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all())

    class Meta:
        model = Attacks
        fields = '__all__'