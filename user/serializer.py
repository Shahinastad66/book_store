from rest_framework import serializers
from user.models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class RegisterUserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone_number", "username", "password", "national_code"]
        extra_kwargs = {"password" : {"write_only": True},
                        "national_code" : {"read_only" : True}
                        }

    def validate_national_code(self, value):
        if len(value) < 10:
            raise

    def create(self, validated_data):
        user = User(
            phone_number = validated_data['phone_number'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['is_author'] = user.is_author
        return token