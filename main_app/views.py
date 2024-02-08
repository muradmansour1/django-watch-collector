from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from .models import Watch, Brand, Band
from .serializers import WatchSerializer, BrandSerializer, BandSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the watch-collector api home route!'}
    return Response(content)
  
class WatchList(generics.ListCreateAPIView):
  serializer_class = WatchSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
      # This ensures we only return cats belonging to the logged-in user
      user = self.request.user
      return Watch.objects.filter(user=user)

  def perform_create(self, serializer):
      # This associates the newly created cat with the logged-in user
      serializer.save(user=self.request.user)

class WatchDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = WatchSerializer
  lookup_field = 'id'

  def get_queryset(self):
    user = self.request.user
    return Watch.objects.filter(user=user)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    band_not_associated = Band.objects.exclude(id__in=instance.band.all())
    band_serializer = BandSerializer(band_not_associated, many=True)

    return Response({
        'watch': serializer.data,
        'band_not_associated': band_serializer.data
    })

  def perform_update(self, serializer):
    watch = self.get_object()
    if watch.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to edit this watch."})
    serializer.save()

  def perform_destroy(self, instance):
    if instance.user != self.request.user:
        raise PermissionDenied({"message": "You do not have permission to delete this watch."})
    instance.delete()

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

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

# User Login
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })

