from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from datetime import datetime



class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProfileGetSerializer(serializers.Serializer):
    date_of_birth = serializers.DateField()
    age = serializers.SerializerMethodField()

    def get_age(self, instance):
        total_seconds = (datetime.now().date() - instance.date_of_birth).total_seconds()
        age = divmod(total_seconds, 31536000)[0] 
        return age


class ProfileSerializer(serializers.Serializer):
    date_of_birth = serializers.DateField()
    email = serializers.EmailField()
    photo = serializers.ImageField()

    def update(self, instance, validated_data):
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
    
        instance.save()
        return instance
