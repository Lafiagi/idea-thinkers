from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class UserLoginSerializer(ModelSerializer):
    email = serializers.CharField( max_length=100, required = True , write_only = True)
    password = serializers.CharField( max_length=100, required = True , write_only = True)
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'phone_number':{'read_only':True},
            'first_name':{'read_only':True},
            'last_name':{'read_only':True},
            'email':{'read_only':True},
            'avatar':{'read_only':True},
            'last_login':{'read_only':True},
        }

class UserSerializer(ModelSerializer):
    first_name = serializers.CharField( max_length=100, required = True , write_only = True)
    last_name = serializers.CharField( max_length=100, required = True , write_only = True)
    phone_number = serializers.CharField( max_length=100, required = True , write_only = True)
    email = serializers.CharField( max_length=100, required = True , write_only = True)
    avatar = serializers.ImageField()
    password = serializers.CharField( max_length=100, required = True , write_only = True)
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'phone_number':{'read_only':True},
            'first_name':{'read_only':True},
            'last_name':{'read_only':True},
            'email':{'read_only':True},
            'avatar':{'read_only':True},
            'last_login':{'read_only':True},
        }

    def to_representation(self, instance):
        rep = super(UserSerializer, self).to_representation(instance)
        rep.pop('password')
        return rep