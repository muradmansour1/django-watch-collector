from rest_framework import serializers
from .models import Watch
from .models import Brand 
from .models import Band
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user

class BandSerializer(serializers.ModelSerializer):
    class Meta:
      model = Band
      fields = '__all__'

class WatchSerializer(serializers.ModelSerializer):
  fed_for_today = serializers.SerializerMethodField()
  band = BandSerializer(many=True, read_only=True) #add this line
  user = serializers.PrimaryKeyRelatedField(read_only=True)
class Meta:
    model = Watch
    fields = '__all__'
        

class BrandSerializer(serializers.ModelSerializer):
  class Meta:
    model = Brand
    fields = '__all__'
    read_only_fields = ('watch',)

