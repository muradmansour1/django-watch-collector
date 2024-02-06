from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Watch, Brand, Band
from .serializers import WatchSerializer, BrandSerializer, BandSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the watch-collector api home route!'}
    return Response(content)
  
class WatchList(generics.ListCreateAPIView):
  queryset = Watch.objects.all()
  serializer_class = WatchSerializer

class WatchDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Watch.objects.all()
  serializer_class = WatchSerializer
  lookup_field = 'id'

class BrandListCreate(generics.ListCreateAPIView):
  serializer_class = BrandSerializer

  def get_queryset(self):
    Watch_id = self.kwargs['Watch_id']
    return Brand.objects.filter(Watch_id=Watch_id)

  def perform_create(self, serializer):
    Watch_id = self.kwargs['Watch_id']
    Watch = Watch.objects.get(id=Watch_id)
    serializer.save(Watch=Watch)

class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
      serializer_class = BrandSerializer
      lookup_field = 'id'

def get_queryset(self):
    Watch_id = self.kwargs['Watch_id']
    return Brand.objects.filter(Watch_id=Watch_id)

class BandList(generics.ListCreateAPIView):
  queryset = Band.objects.all()
  serializer_class = BandSerializer

class BandDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Band.objects.all()
  serializer_class = BandSerializer
  lookup_field = 'id'
