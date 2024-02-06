from rest_framework import serializers
from .models import Watch
from .models import Brand 
from .models import Band

class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = '__all__'
        

class BrandSerializer(serializers.ModelSerializer):
  class Meta:
    model = Brand
    fields = '__all__'
    read_only_fields = ('watch',)

class BandSerializer(serializers.ModelSerializer):
    class Meta:
      model = Band
      fields = '__all__'
