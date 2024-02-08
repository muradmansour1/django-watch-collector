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

  # add (override) the retrieve method below
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    # Get the list of toys not associated with this cat
    band_not_associated = Band.objects.exclude(id__in=instance.band.all())
    band_serializer = BandSerializer(band_not_associated, many=True)

    return Response({
        'watch': serializer.data,
        'band_not_associated': band_serializer.data
    })

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

class AddBandToWatch(APIView):
  def post(self, request, watch_id, band_id):
    watch = Watch.objects.get(id=watch_id)
    band = Band.objects.get(id=band_id)
    watch.band.add(band)
    return Response({'message': f'Band {band.name} added to Watch {watch.name}'})

