from rest_framework import serializers
from .models import Watch
from .models import Brand 
from .models import Band

class BandSerializer(serializers.ModelSerializer):
    class Meta:
      model = Band
      fields = '__all__'

class WatchSerializer(serializers.ModelSerializer):
  fed_for_today = serializers.SerializerMethodField()
  band = BandSerializer(many=True, read_only=True) #add this line
class Meta:
    model = Watch
    fields = '__all__'
        

class BrandSerializer(serializers.ModelSerializer):
  class Meta:
    model = Brand
    fields = '__all__'
    read_only_fields = ('watch',)

